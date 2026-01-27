use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;

use grammers_mtsender_pyo3::InvocationError;

use crate::client::PyClient;
use crate::errors::InvocationErrorConverter;
use grammers_session_pyo3::{PyPeerAuth, PyPeerId, PyPeerInfo, PyUpdateState, PyUpdatesState};
use grammers_tl_types_pyo3 as pytl;
use grammers_tl_types_pyo3::{PyTLObject, PyTLRequest};

#[pymethods]
impl PyClient {
    pub async fn is_authorized(&self) -> PyResult<bool> {
        let request = pytl::functions::updates::PyGetState {};
        match self.invoke_raw(request.into()).await {
            Ok(_) => Ok(true),
            Err(InvocationError::Rpc(e)) if e.code == 401 => Ok(false),
            Err(err) => Err(InvocationErrorConverter(err).into()),
        }
    }

    /// Terminal interactive login.
    pub async fn authorize(&mut self) -> PyResult<bool> {
        if self.inner.lock().unwrap().bot_token.is_some() {
            self.me = Some(self.bot_sign_in(None).await?);
            return Ok(true);
        }

        Ok(true)
    }

    /// Signs in to the bot account associated with this token.
    ///
    /// This is the method you need to call to use the client under a bot account.
    ///
    /// It is recommended to save the session on successful login. Some session storages will do this
    /// automatically. If saving fails, it is recommended to [`Client::sign_out`]. If the session is never
    /// saved post-login, then the authorization will be "lost" in the list of logged-in clients, since it
    /// is unaccessible.
    ///
    /// # Examples
    ///
    /// ```
    /// # Note: these values are obviously fake.
    /// # Obtain your own with the developer's phone at https://my.telegram.org.
    /// API_HASH: str = "514727c32270b9eb8cc16daf17e21e57"
    /// # Obtain your own by talking to @BotFather via a Telegram app.
    /// BOT_TOKEN: str = "776609994:AAFXAy5-PawQlnYywUlZ_b_GOXgarR3ah_yq"
    ///
    /// client = Client('bot', API_ID, API_HASH, bot_token=BOT_TOKEN)
    /// async def main():
    ///     user = await client.bot_sign_in()
    ///     print('Signed in as {user.first_name}')
    /// ```
    #[pyo3(signature = (bot_token=None))]
    pub async fn bot_sign_in(&self, bot_token: Option<String>) -> PyResult<pytl::enums::PyUser> {
        let token = match bot_token {
            Some(x) => x,
            None => self
                .inner
                .lock()
                .unwrap()
                .bot_token
                .clone()
                .ok_or_else(|| PyValueError::new_err("bot_token is not provided."))?,
        };
        let request: PyTLRequest = pytl::functions::auth::PyImportBotAuthorization {
            flags: 0,
            api_id: self.inner.lock().unwrap().api_id,
            api_hash: self.inner.lock().unwrap().api_hash.clone(),
            bot_auth_token: token,
        }
        .into();

        let result = match self.invoke_raw(request.clone()).await {
            Ok(x) => x,
            Err(InvocationError::Rpc(err)) if err.code == 303 => {
                let session = self.inner.lock().unwrap().session.clone();
                let old_dc_id = session.home_dc_id().await?;
                let new_dc_id = err.value.unwrap() as i32;
                // Disconnect from current DC to cull the now-unused connection.
                // This also gives a chance for the new home DC to export its authorization
                // if there's a need to connect back to the old DC after having logged in.
                self.inner
                    .lock()
                    .unwrap()
                    .handle
                    .disconnect_from_dc(old_dc_id);
                session.set_home_dc_id(new_dc_id).await?;
                self.invoke(request).await?
            }
            Err(e) => return Err(InvocationErrorConverter(e).into()),
        };

        match result {
            PyTLObject::auth_Authorization(x) => self.complete_login(x).await,
            PyTLObject::auth_AuthorizationSignUpRequired(_) => Err(PyRuntimeError::new_err(
                "API returned SignUpRequired even though we're logging in as a bot",
            )),
            _ => {
                panic!("no expect API return");
            }
        }
    }

    /// Signs out of the account authorized by this client's session.
    ///
    /// If the client was not logged in, this method raise RpcError.
    ///
    /// The client is not disconnected after signing out.
    ///
    /// Note that after using this method you will have to sign in again. If all you want to do
    /// is disconnect, simply call `await client.stop()`.
    ///
    /// # Examples
    ///
    /// ```
    /// from grammers import errors
    ///
    /// try:
    ///     await client.sign_out()
    /// except errors.RpcError:
    ///     println!("No user was signed in, so nothing has changed...");
    /// else:
    ///     println!("Signed out successfully!");
    /// ```
    pub async fn sign_out(&self) -> PyResult<PyTLObject> {
        let request = pytl::functions::auth::PyLogOut {};
        self.invoke(request.into()).await
    }

    pub fn disconnect(&self) {
        self.inner.lock().unwrap().handle.quit();
    }
}

impl PyClient {
    async fn complete_login(
        &self,
        auth: pytl::types::auth::PyAuthorizationWrapper,
    ) -> PyResult<pytl::enums::PyUser> {
        // In the extremely rare case where `Err` happens, there's not much we can do.
        // `message_box` will try to correct its state as updates arrive.
        let update_state = self
            .invoke_raw(pytl::functions::updates::PyGetState {}.into())
            .await
            .ok();

        let user = Python::attach(|py| auth.0.borrow(py).user.clone());
        let (user_id, bot) = match user {
            pytl::enums::PyUser::User(ref u) => Python::attach(|py| {
                let u = u.0.borrow(py);
                (u.id, Some(u.bot))
            }),
            pytl::enums::PyUser::Empty(ref u) => Python::attach(|py| (u.0.borrow(py).id, None)),
        };
        let session = self.inner.lock().unwrap().session.clone();
        let auth = match user {
            pytl::enums::PyUser::User(ref u) => Python::attach(|py| {
                let u = u.0.borrow(py);
                u.access_hash.filter(|_| !u.min).map(PyPeerAuth::new)
            }),
            pytl::enums::PyUser::Empty(_) => {
                let peer = session.peer(PyPeerId::user(user_id)?).await?;
                match peer {
                    Some(p) => p.auth(),
                    None => None,
                }
            }
        };

        session
            .cache_peer(PyPeerInfo::User {
                id: user_id,
                auth: auth,
                bot,
                is_self: Some(true),
            })
            .await?;
        if let Some(PyTLObject::updates_State(state)) = update_state {
            let state = Python::attach(|py| state.0.borrow(py).clone());
            session
                .set_update_state(PyUpdateState::All(PyUpdatesState {
                    pts: state.pts,
                    qts: state.qts,
                    date: state.date,
                    seq: state.seq,
                    channels: Vec::new(),
                }))
                .await?;
        }

        Ok(user)
    }
}
