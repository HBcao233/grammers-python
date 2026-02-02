use pyo3::create_exception;
use pyo3::exceptions::{PyException, PyRuntimeError, PyValueError};
use pyo3::prelude::*;

use grammers_crypto::two_factor_auth::{calculate_2fa, check_p_and_g};
use grammers_mtsender_pyo3::InvocationError;
use grammers_session_pyo3::{PyPeerAuth, PyPeerId, PeerInfoLike, PyUpdatesState, UpdateStateLike};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use crate::client::PyClient;
use crate::errors::PyInvocationError;
use crate::utils::extract_password_parameters;
use crate::peer::PyUser;

/// Login token needed to continue the login process after sending the code.
#[derive(Clone)]
#[pyclass(name = "LoginToken", module = "grammers")]
pub struct PyLoginToken {
    #[pyo3(get, set)]
    pub phone: String,
    #[pyo3(get, set)]
    pub phone_code_hash: String,
}
#[pymethods]
impl PyLoginToken {
    #[new]
    fn __new__(phone: String, phone_code_hash: String) -> Self {
        Self {
            phone,
            phone_code_hash,
        }
    }

    fn __repr__(&self) -> String {
        format!(
            "LoginToken(\n  phone={},\n  phone_code_hash={},\n)",
            pytl::utils::mask_phone(&self.phone),
            self.phone_code_hash,
        )
    }
}

create_exception!(
    grammers.errors,
    SignInError,
    PyException,
    "Login-related errors."
);
create_exception!(
    grammers.errors,
    PaymentRequiredError,
    SignInError,
    "Indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a Telegram Premium subscription in order to proceed with the login/signup."
);
create_exception!(
    grammers.errors,
    SignUpRequiredError,
    SignInError,
    "Sign-up with an official client is required. (Third-party applications cannot be used to register new accounts.)"
);
create_exception!(
    grammers.errors,
    PasswordRequiredError,
    SignInError,
    "The account has 2FA enabled, and the password is required."
);
create_exception!(
    grammers.errors,
    InvalidCodeError,
    SignInError,
    "The code used to complete login was not valid."
);
create_exception!(
    grammers.errors,
    InvalidPasswordError,
    SignInError,
    "The 2FA password used to complete login was not valid."
);

pub struct PyPaymentRequiredError {}
impl PyPaymentRequiredError {
    pub fn new() -> PyErr {
        PaymentRequiredError::new_err(
            "Indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a Telegram Premium subscription in order to proceed with the login/signup.",
        )
    }
}

pub struct PySignUpRequiredError {}
impl PySignUpRequiredError {
    pub fn new() -> PyErr {
        SignUpRequiredError::new_err(
            "Sign-up with an official client is required. (Third-party applications cannot be used to register new accounts.)",
        )
    }
}

pub struct PyPasswordRequiredError {}
impl PyPasswordRequiredError {
    pub fn new() -> PyErr {
        PasswordRequiredError::new_err("The account has 2FA enabled, and the password is required.")
    }
}

pub struct PyInvalidCodeError {}
impl PyInvalidCodeError {
    pub fn new() -> PyErr {
        InvalidCodeError::new_err("The code used to complete login was not valid.")
    }
}

pub struct PyInvalidPasswordError {}
impl PyInvalidPasswordError {
    pub fn new() -> PyErr {
        InvalidPasswordError::new_err("The 2FA password used to complete login was not valid.")
    }
}

#[pymethods]
impl PyClient {
    /// Returns `true` if the current account is authorized. Otherwise,
    /// logging in will be required before being able to invoke requests.
    ///
    /// This will likely be the first method you want to call on a connected [`Client`]. After you
    /// determine if the account is authorized or not, you will likely want to use either
    /// [`Client.bot_sign_in`] or [`Client.request_login_code`].
    ///
    /// # Examples
    ///
    /// ```ignore
    /// if await client.is_authorized():
    ///     print('Client already authorized and ready to use!')
    /// else:
    ///     print('Client is not authorized, you will need to sign_in!')
    /// ```
    pub async fn is_authorized(&self) -> PyResult<bool> {
        let request = tl::functions::updates::GetState {};
        match self.invoke(&request).await {
            Ok(_) => Ok(true),
            Err(InvocationError::Rpc(e)) if e.code == 401 => Ok(false),
            Err(err) => Err(PyInvocationError::new(err)),
        }
    }

    /// Terminal interactive login.
    pub async fn authorize(&self) -> PyResult<Py<PyUser>> {
        let bot_token = self.bot_token();
        if bot_token.is_some() {
            return Ok(self.bot_sign_in(bot_token).await?);
        }

        // check if session is logined
        let session = self.session();
        let dc_id = session.home_dc_id().await?;
        let dc_option = session.dc_option(dc_id).await?;
        if dc_option.is_some() && dc_option.unwrap().auth_key.is_some() {
            if let Ok(x) = self.get_password_information().await {
                return self._check_password(Some(x.into())).await;
            }
        }

        let phone = self.phone();
        let phone = crate::utils::maybe_call0(phone)?;
        let phone = crate::utils::maybe_await(phone).await?;
        let phone: String = Python::attach(|py| phone.bind(py).extract())?;

        let api_hash = self.api_hash();
        let login_token = self.request_login_code(phone, api_hash).await?;

        let code = Python::attach(|py| self.code().call0(py))?;
        let code = crate::utils::maybe_await(code).await?;
        let code = Python::attach(|py| code.bind(py).str().map(|x| x.to_string()))?;

        let user = match self.sign_in(login_token, code).await {
            Ok(user) => Ok(user),
            Err(e) if Python::attach(|py| e.is_instance_of::<PasswordRequiredError>(py)) => {
                self._check_password(None).await
            },
            Err(e) => Err(e),
        }?;

        Ok(user)
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
    /// ```ignore
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
    pub async fn bot_sign_in(&self, bot_token: Option<String>) -> PyResult<Py<PyUser>> {
        let token = match bot_token {
            Some(x) => x,
            None => self
                .bot_token()
                .ok_or_else(|| PyValueError::new_err("bot_token is not provided."))?,
        };
        let request = tl::functions::auth::ImportBotAuthorization {
            flags: 0,
            api_id: self.api_id(),
            api_hash: self.api_hash(),
            bot_auth_token: token,
        };

        let result = match self.invoke(&request).await {
            Ok(x) => x,
            Err(InvocationError::Rpc(err)) if err.code == 303 => {
                let session = self.session();
                let old_dc_id = session.home_dc_id().await?;
                let new_dc_id = err.value.unwrap() as i32;
                // Disconnect from current DC to cull the now-unused connection.
                // This also gives a chance for the new home DC to export its authorization
                // if there's a need to connect back to the old DC after having logged in.
                self.handle().disconnect_from_dc(old_dc_id);
                session.set_home_dc_id(new_dc_id).await?;
                self.invoke(&request)
                    .await
                    .map_err(PyInvocationError::new)?
            }
            Err(e) => return Err(PyInvocationError::new(e)),
        };

        match result {
            tl::enums::auth::Authorization::Authorization(x) => self._complete_login(x.into()).await,
            tl::enums::auth::Authorization::SignUpRequired(_) => Err(PyRuntimeError::new_err(
                "API returned SignUpRequired even though we're logging in as a bot",
            )),
        }
    }

    /// Requests the login code for the account associated to the given phone
    /// number via another Telegram application or SMS.
    ///
    /// This is the method you need to call before being able to sign in to a user account.
    /// After you obtain the code and it's inside your program (e.g. ask the user to enter it
    /// via the console's standard input), you will need to [`Client::sign_in`] to complete the
    /// process.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// # Note: these values are obviously fake.
    /// # Obtain your own with the developer's phone at https://my.telegram.org.
    /// API_HASH: str = "514727c32270b9eb8cc16daf17e21e57"
    /// # The phone used here does NOT need to be the same as the one used by the developer
    /// # to obtain the API ID and hash.
    /// PHONE: str = "+1 415 555 0132"
    ///
    /// if not await client.is_authorized():
    ///     # We're not logged in, so request the login code.
    ///     token = await client.request_login_code(PHONE, API_HASH)
    /// ```
    pub async fn request_login_code(
        &self,
        phone: String,
        api_hash: String,
    ) -> PyResult<PyLoginToken> {
        let request = tl::functions::auth::SendCode {
            phone_number: phone.to_string(),
            api_id: self.api_id(),
            api_hash: api_hash.to_string(),
            settings: tl::types::CodeSettings {
                allow_flashcall: false,
                current_number: false,
                allow_app_hash: false,
                allow_missed_call: false,
                allow_firebase: false,
                logout_tokens: None,
                token: None,
                app_sandbox: None,
                unknown_number: false,
            }
            .into(),
        };

        use tl::enums::auth::SentCode as SC;

        let sent_code: tl::types::auth::SentCode = match self.invoke(&request).await {
            Ok(x) => match x {
                SC::Code(code) => code,
                SC::Success(_) => {
                    return Err(SignInError::new_err(
                        "Sign-in success even if we don't provided any future auth tokens.",
                    ));
                }
                SC::PaymentRequired(_) => return Err(PyPaymentRequiredError::new()),
            },
            Err(InvocationError::Rpc(err)) if err.code == 303 => {
                let session = self.session();
                let old_dc_id = session.home_dc_id().await?;
                let new_dc_id = err.value.unwrap() as i32;
                // Disconnect from current DC to cull the now-unused connection.
                // This also gives a chance for the new home DC to export its authorization
                // if there's a need to connect back to the old DC after having logged in.
                self.handle().disconnect_from_dc(old_dc_id);
                session.set_home_dc_id(new_dc_id).await?;
                match self
                    .invoke(&request)
                    .await
                    .map_err(PyInvocationError::new)?
                {
                    SC::Code(code) => code,
                    SC::Success(_) => {
                        return Err(SignInError::new_err(
                            "Sign-in success even if we don't provided any future auth tokens.",
                        ));
                    }
                    SC::PaymentRequired(_) => return Err(PyPaymentRequiredError::new()),
                }
            }
            Err(e) => return Err(PyInvocationError::new(e)),
        };

        Ok(PyLoginToken {
            phone: phone.to_string(),
            phone_code_hash: sent_code.phone_code_hash,
        })
    }

    /// Signs in to the user account.
    ///
    /// You must call [`Client.request_login_code`] before using this method in order to obtain
    /// necessary login token, and also have asked the user for the login code.
    ///
    /// It is recommended to save the session on successful login. Some session storages will do this
    /// automatically. If saving fails, it is recommended to [`Client.sign_out`]. If the session is never
    /// saved post-login, then the authorization will be "lost" in the list of logged-in clients, since it
    /// is unaccessible.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// # API_HASH: str = ""
    /// # PHONE: str = ""
    /// def ask_code_to_user() -> str:
    ///     pass
    ///
    /// token = await client.request_login_code(PHONE, API_HASH)
    /// code = ask_code_to_user()
    ///
    /// try:
    ///     let user = await client.sign_in(token, code)
    /// except errors.PasswordRequiredError as e:
    ///     token = e.token
    ///     print('Please provide a password)
    /// except errors.SignUpRequiredError:
    ///     print('Sign up required')
    /// except errors.RPCError as e:
    ///     print('Failed to sign in as a user:\n', traceback.format_exc(e))
    ///
    /// if user.first_name:
    ///     print(f"Signed in as {user.first_name}!")
    /// else:
    ///     println!("Signed in!")
    /// ```
    pub async fn sign_in(
        &self,
        token: PyLoginToken,
        code: String,
    ) -> PyResult<Py<PyUser>> {
        match self
            .invoke(&tl::functions::auth::SignIn {
                phone_number: token.phone.clone(),
                phone_code_hash: token.phone_code_hash.clone(),
                phone_code: Some(code.to_string()),
                email_verification: None,
            })
            .await
        {
            Ok(tl::enums::auth::Authorization::Authorization(x)) => self._complete_login(x.into()).await,
            Ok(tl::enums::auth::Authorization::SignUpRequired(_)) => {
                Err(PySignUpRequiredError::new())
            }
            Err(err) if err.is("SESSION_PASSWORD_NEEDED") => Err(PyPasswordRequiredError::new()),
            Err(err) if err.is("PHONE_CODE_*") => Err(PyInvalidCodeError::new()),
            Err(error) => Err(PyInvocationError::new(error)),
        }
    }

    /// Extract information needed for the two-factor authentication
    /// It's called automatically when we get SESSION_PASSWORD_NEEDED error during sign in.
    pub async fn get_password_information(&self) -> PyResult<pytl::enums::account::PyPassword> {
        let request = tl::functions::account::GetPassword {};

        let password = self
            .invoke(&request)
            .await
            .map_err(PyInvocationError::new)?;

        Ok(password.into())
    }

    /// Sign in using two-factor authentication (user password).
    ///
    /// [`password_token`] can be obtained from [`PasswordRequiredError`] error after the
    /// [`Client.sign_in`] method fails.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// # const API_HASH: &str = "";
    /// # const PHONE: &str = "";
    /// def get_user_password(hint: str) -> String:
    ///     pass
    ///
    /// # let token = await client.request_login_code(PHONE, API_HASH)
    /// # let code = "";
    ///
    /// # ... enter phone number, request login code ...
    ///
    /// try:
    ///     let user = await client.sign_in(token, code)
    /// except errors.PasswordRequiredError as e:
    ///     password_token = e.password_token
    ///     password = get_user_password(password_token.hint)
    ///
    ///     try:
    ///         user = await client.check_password(password_token, password)
    ///     except errors.RpcError as e:
    ///         print('Sign in required')
    /// except errors.RpcError as e:
    ///     print('Failed to sign in as a user:', traceback.format_exc(e))
    ///
    /// ```
    pub async fn check_password(
        &self,
        password_info: pytl::types::account::PyPassword,
        password: String,
    ) -> PyResult<Py<PyUser>> {
        let mut password_info: tl::types::account::Password = password_info.into();
        let current_algo = password_info.current_algo.as_ref().unwrap();
        let mut params = extract_password_parameters(&current_algo);

        // Telegram sent us incorrect parameters, trying to get them again
        if !check_p_and_g(params.2, params.3) {
            password_info = match self.get_password_information().await? {
                pytl::enums::account::PyPassword::Password(x) => x.into(),
            };
            let current_algo = password_info.current_algo.as_ref().unwrap();
            params = extract_password_parameters(&current_algo);
            if !check_p_and_g(params.2, params.3) {
                return Err(PyValueError::new_err(
                    "Failed to get correct password information from Telegram",
                ));
            }
        }

        let (salt1, salt2, p, g) = params;

        let g_b = password_info.srp_b.clone().unwrap();
        let a = password_info.secure_random.clone();

        let (m1, g_a) = calculate_2fa(salt1, salt2, p, g, g_b, a, password);

        let check_password = tl::functions::auth::CheckPassword {
            password: tl::enums::InputCheckPasswordSrp::Srp(tl::types::InputCheckPasswordSrp {
                srp_id: password_info.srp_id.clone().unwrap(),
                a: g_a.to_vec(),
                m1: m1.to_vec(),
            }),
        };

        match self.invoke(&check_password).await {
            Ok(tl::enums::auth::Authorization::Authorization(x)) => self._complete_login(x.into()).await,
            Ok(tl::enums::auth::Authorization::SignUpRequired(_x)) => {
                Err(PySignUpRequiredError::new())
            }
            Err(err) if err.is("PASSWORD_HASH_INVALID") => Err(PyInvalidPasswordError::new()),
            Err(error) => Err(PyInvocationError::new(error)),
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
    /// ```ignore
    /// from grammers import errors
    ///
    /// try:
    ///     await client.sign_out()
    /// except errors.RpcError:
    ///     print("No user was signed in, so nothing has changed...");
    /// else:
    ///     print("Signed out successfully!");
    /// ```
    pub async fn sign_out(&self) -> PyResult<pytl::enums::auth::PyLoggedOut> {
        let request = pytl::functions::auth::PyLogOut {};
        self.invoke(&request).await.map_err(PyInvocationError::new)
    }

    /// Signals all clients sharing the same sender pool to disconnect.
    pub fn disconnect(&self) {
        self.inner.lock().unwrap().handle.quit();
    }

    #[pyo3(signature = (password_info=None))]
    async fn _check_password(
        &self,
        password_info: Option<pytl::enums::account::PyPassword>,
    ) -> PyResult<Py<PyUser>> {
        let password_info = match password_info {
            Some(x) => x,
            None => self.get_password_information().await?,
        };
        let password_info: pytl::types::account::PyPassword = match password_info {
            pytl::enums::account::PyPassword::Password(x) => {
                Python::attach(|py| x.0.borrow(py).clone())
            }
        };
        let hint = password_info.hint.clone();

        let password = self.password();
        let password = Python::attach(|py| crate::utils::maybe_call1(py, password, (hint,)))?;
        let password = crate::utils::maybe_await(password).await?;
        let password: String = Python::attach(|py| password.bind(py).extract())?;

        self.check_password(password_info, password).await
    }

    async fn _complete_login(
        &self,
        auth: pytl::types::auth::PyAuthorization,
    ) -> PyResult<Py<PyUser>> {
        let auth: tl::types::auth::Authorization = auth.into();
        let user = auth.user;
        let user_id = user.id();
        let bot = match user {
            tl::enums::User::User(ref u) => Some(u.bot),
            tl::enums::User::Empty(_) => None,
        };
        let session = self.session();
        let auth = match user {
            tl::enums::User::User(ref u) => u.access_hash.filter(|_| !u.min).map(PyPeerAuth::new),
            tl::enums::User::Empty(_) => {
                let peer = session.peer(PyPeerId::user(user_id)?).await?;
                match peer {
                    Some(p) => p.auth(),
                    None => None,
                }
            }
        };

        session
            .cache_peer(PeerInfoLike::User {
                id: user_id,
                auth: auth,
                bot,
                is_self: Some(true),
            })
            .await?;

        // In the extremely rare case where `Err` happens, there's not much we can do.
        // `message_box` will try to correct its state as updates arrive.
        let update_state = self
            .invoke(&tl::functions::updates::GetState {})
            .await;
        if let Ok(tl::enums::updates::State::State(state)) = update_state {
            session
                .set_update_state(UpdateStateLike::All(PyUpdatesState {
                    pts: state.pts,
                    qts: state.qts,
                    date: state.date,
                    seq: state.seq,
                    channels: Vec::new(),
                }))
                .await?;
        }

        Python::attach(|py|
            Py::new(py, PyUser::new(self, user.into()))
        )
    }
}
