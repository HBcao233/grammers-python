use pyo3::prelude::*;

use std::collections::VecDeque;
use std::time::{Duration, Instant};

use grammers_mtsender_pyo3::InvocationError;
use grammers_session_pyo3::{Session, PyPeerId, PyPeerInfo, PyUpdateState, PyUpdatesState};
use grammers_session::updates::{MessageBoxes, PrematureEndReason, State, UpdatesLike};
use grammers_tl_types as tl;

use log::{trace, warn};
use tokio::sync::mpsc;
use tokio::time::timeout_at;

use super::PyClient;
use crate::peer::PeerMap;
// use grammers_client::update::Update;

/// How long to wait after warning the user that the updates limit was exceeded.
const UPDATE_LIMIT_EXCEEDED_LOG_COOLDOWN: Duration = Duration::from_secs(300);

// See https://core.telegram.org/method/updates.getChannelDifference.
const BOT_CHANNEL_DIFF_LIMIT: i32 = 100000;
const USER_CHANNEL_DIFF_LIMIT: i32 = 100;

/// Configuration that controls [`Client::stream_updates`].
pub struct UpdatesConfiguration {
    /// Should the client catch-up on updates sent to it while it was offline?
    ///
    /// By default, updates sent while the client was offline are ignored.
    pub catch_up: bool,

    /// How many updates may be buffered by the client at any given time.
    ///
    /// Telegram passively sends updates to the client through the open connection, so they must
    /// be buffered until the application has the capacity to consume them.
    ///
    /// Upon reaching this limit, updates will be dropped, and a warning log message will be
    /// emitted (but not too often, to avoid spamming the log), in order to let the developer
    /// know that they should either change how they handle updates or increase the limit.
    ///
    /// A limit of zero (`Some(0)`) indicates that updates should not be buffered.
    /// They will be immediately dropped, and no warning will ever be emitted.
    ///
    /// A limit of `None` disables the upper bound for the buffer. This is not recommended, as it
    /// could eventually lead to memory exhaustion. This option will also not emit any warnings.
    ///
    /// The default limit, which may change at any time, should be enough for user accounts,
    /// although bot accounts may need to increase the limit depending on their capacity.
    ///
    /// When the limit is `Some`, a buffer to hold that many updates will be pre-allocated.
    pub update_queue_limit: Option<usize>,
}

async fn prepare_channel_difference(
    mut request: tl::functions::updates::GetChannelDifference,
    session: Session,
    message_box: &mut MessageBoxes,
) -> PyResult<Option<tl::functions::updates::GetChannelDifference>> {
    let id = match &request.channel {
        tl::enums::InputChannel::Channel(channel) => PyPeerId::channel(channel.channel_id)?,
        _ => unreachable!(),
    };

    if let Some(PyPeerInfo::Channel {
        id,
        auth: Some(auth),
        ..
    }) = session.peer(id).await?
    {
        request.channel = tl::enums::InputChannel::Channel(tl::types::InputChannel {
            channel_id: id,
            access_hash: auth.hash(),
        });
        request.limit = if session
            .peer(PyPeerId::self_user()?)
            .await?
            .map(|user| match user {
                PyPeerInfo::User { bot, .. } => bot.unwrap_or(false),
                _ => false,
            })
            .unwrap_or(false)
        {
            BOT_CHANNEL_DIFF_LIMIT
        } else {
            USER_CHANNEL_DIFF_LIMIT
        };
        trace!("requesting {:?}", request);
        Ok(Some(request))
    } else {
        warn!(
            "cannot getChannelDifference for {:?} as we're missing its hash",
            id
        );
        message_box.end_channel_difference(PrematureEndReason::Banned);
        Ok(None)
    }
}

/// Iterator returned by [`Client::stream_updates`].
pub struct UpdateStream {
    client: PyClient,
    message_box: MessageBoxes,
    // When did we last warn the user that the update queue filled up?
    // This is used to avoid spamming the log.
    last_update_limit_warn: Option<Instant>,
    buffer: VecDeque<(tl::enums::Update, State, PeerMap)>,
    updates: mpsc::UnboundedReceiver<UpdatesLike>,
    configuration: UpdatesConfiguration,
    should_get_state: bool,
}

impl UpdateStream {
    /// Pops an update from the queue, waiting for an update to arrive first if the queue is empty.
    /*pub async fn next(&mut self) -> Result<Update, InvocationError> {
        let (update, state, peers) = self.next_raw().await?;
        Ok(Update::from_raw(&self.client, update, state, peers))
    }*/

    /// Pops an update from the queue, waiting for an update to arrive first if the queue is empty.
    ///
    /// Unlike [`Self::next`], the update is not wrapped at all, but it is still processed.
    pub async fn next_raw(
        &mut self,
    ) -> Result<(tl::enums::Update, State, PeerMap), InvocationError> {
        if self.should_get_state {
            self.should_get_state = false;
            match self
                .client
                .invoke_tl(&tl::functions::updates::GetState {})
                .await
            {
                Ok(tl::enums::updates::State::State(state)) => {
                    self.client
                        .inner
                        .lock()
                        .unwrap()
                        .session
                        .set_update_state(PyUpdateState::All(PyUpdatesState {
                            pts: state.pts,
                            qts: state.qts,
                            date: state.date,
                            seq: state.seq,
                            channels: Vec::new(),
                        }))
                        .await
                        .map_err(|e| InvocationError::PyErr(e))?;
                }
                Err(_err) => {
                    // The account may no longer actually be logged in, or it can rarely fail.
                    // `message_box` will try to correct its state as updates arrive.
                }
            }
        }

        loop {
            let (deadline, get_diff, get_channel_diff) = {
                if let Some(update) = self.buffer.pop_front() {
                    return Ok(update);
                }
                let session = self.client.inner.lock().unwrap().session.clone();
                (
                    self.message_box.check_deadlines(), // first, as it might trigger differences
                    self.message_box.get_difference(),
                    match self.message_box.get_channel_difference() {
                        Some(gd) => {
                            prepare_channel_difference(
                                gd,
                                session,
                                &mut self.message_box,
                            )
                            .await.map_err(|e| InvocationError::PyErr(e))?
                        }
                        None => None,
                    },
                )
            };

            if let Some(request) = get_diff {
                let response = self.client.invoke_tl(&request).await?;
                let (updates, users, chats) = self.message_box.apply_difference(response);
                let peers = self.client.build_peer_map(users, chats).await.map_err(|e| InvocationError::PyErr(e))?;
                self.extend_update_queue(updates, peers);
                continue;
            }

            if let Some(request) = get_channel_diff {
                let maybe_response = self.client.invoke_tl(&request).await;

                let response = match maybe_response {
                    Ok(r) => r,
                    Err(e) if e.is("PERSISTENT_TIMESTAMP_OUTDATED") => {
                        // According to Telegram's docs:
                        // "Channel internal replication issues, try again later (treat this like an RPC_CALL_FAIL)."
                        // We can treat this as "empty difference" and not update the local pts.
                        // Then this same call will be retried when another gap is detected or timeout expires.
                        //
                        // Another option would be to literally treat this like an RPC_CALL_FAIL and retry after a few
                        // seconds, but if Telegram is having issues it's probably best to wait for it to send another
                        // update (hinting it may be okay now) and retry then.
                        //
                        // This is a bit hacky because MessageBox doesn't really have a way to "not update" the pts.
                        // Instead we manually extract the previously-known pts and use that.
                        log::warn!(
                            "Getting difference for channel updates caused PersistentTimestampOutdated; ending getting difference prematurely until server issues are resolved"
                        );
                        {
                            self.message_box
                                .end_channel_difference(PrematureEndReason::TemporaryServerIssues);
                        }
                        continue;
                    }
                    Err(e) if e.is("CHANNEL_PRIVATE") => {
                        log::info!(
                            "Account is now banned so we can no longer fetch updates with request: {:?}",
                            request
                        );
                        {
                            self.message_box
                                .end_channel_difference(PrematureEndReason::Banned);
                        }
                        continue;
                    }
                    Err(InvocationError::Rpc(rpc_error)) if rpc_error.code == 500 => {
                        log::warn!("Telegram is having internal issues: {:#?}", rpc_error);
                        {
                            self.message_box
                                .end_channel_difference(PrematureEndReason::TemporaryServerIssues);
                        }
                        continue;
                    }
                    Err(e) => return Err(e),
                };

                let (updates, users, chats) = self.message_box.apply_channel_difference(response);

                let peers = self.client.build_peer_map(users, chats).await.map_err(|e| InvocationError::PyErr(e))?;
                self.extend_update_queue(updates, peers);
                continue;
            }

            match timeout_at(deadline.into(), self.updates.recv()).await {
                Ok(Some(updates)) => self.process_socket_updates(updates).await.map_err(|e| InvocationError::PyErr(e))?,
                Ok(None) => break Err(InvocationError::Dropped),
                Err(_) => {}
            }
        }
    }

    pub(crate) async fn process_socket_updates(&mut self, updates: UpdatesLike) -> PyResult<()> {
        let mut result = Option::<(Vec<_>, Vec<_>, Vec<_>)>::None;
        match self.message_box.process_updates(updates) {
            Ok(tup) => {
                if let Some(res) = result.as_mut() {
                    res.0.extend(tup.0);
                    res.1.extend(tup.1);
                    res.2.extend(tup.2);
                } else {
                    result = Some(tup);
                }
            }
            Err(_) => return Ok(()),
        }

        if let Some((updates, users, chats)) = result {
            let peers = self.client.build_peer_map(users, chats).await?;
            self.extend_update_queue(updates, peers);
        }
        Ok(())
    }

    fn extend_update_queue(
        &mut self,
        mut updates: Vec<(tl::enums::Update, State)>,
        peer_map: PeerMap,
    ) {
        if let Some(limit) = self.configuration.update_queue_limit {
            if let Some(exceeds) = (self.buffer.len() + updates.len()).checked_sub(limit + 1) {
                let exceeds = exceeds + 1;
                let now = Instant::now();
                let notify = match self.last_update_limit_warn {
                    None => true,
                    Some(instant) => now - instant > UPDATE_LIMIT_EXCEEDED_LOG_COOLDOWN,
                };

                updates.truncate(updates.len() - exceeds);
                if notify {
                    log::warn!(
                        "{} updates were dropped because the update_queue_limit was exceeded",
                        exceeds
                    );
                }

                self.last_update_limit_warn = Some(now);
            }
        }

        self.buffer
            .extend(updates.into_iter().map(|(u, s)| (u, s, peer_map.handle())));
    }

    /// Synchronize the updates state to the session.
    ///
    /// This is **not** automatically done on drop.
    pub async fn sync_update_state(&self) -> PyResult<()> {
        let session = self.client.inner.lock().unwrap().session.clone();
        let update = PyUpdateState::All(self.message_box.session_state().into());
        session.set_update_state(update).await
    }
}

impl PyClient {
    /// Returns an asynchronous stream of processed updates.
    ///
    /// The updates are guaranteed to be in order, and any gaps will be resolved.\
    /// **Important** to note that for gaps to be resolved, the peers must have been
    /// persisted in the session cache beforehand (i.e. be retrievable with [`Session::peer`]).
    /// A good way to achieve this is to use [`Self::iter_dialogs`] at least once after login.
    ///
    /// The updates are wrapped in [`crate::update::Update`] to make them more convenient to use,
    /// but their raw type is still accessible to bridge any missing functionality.
    pub async fn stream_updates(
        &self,
        updates: mpsc::UnboundedReceiver<UpdatesLike>,
        configuration: UpdatesConfiguration,
    ) -> PyResult<UpdateStream> {
        let session = &self.inner.lock().unwrap().session;
        let message_box = if configuration.catch_up {
            MessageBoxes::load(session.updates_state().await?.into())
        } else {
            // If the user doesn't want to bother with catching up on previous update, start with
            // pristine state instead.
            MessageBoxes::new()
        };
        
        // Don't bother getting pristine update state if we're not logged in.
        let should_get_state =
            message_box.is_empty() && session.peer(PyPeerId::self_user()?).await?.is_some();

        Ok(UpdateStream {
            client: self.clone(),
            message_box,
            last_update_limit_warn: None,
            buffer: VecDeque::new(),
            updates,
            configuration,
            should_get_state,
        })
    }
}
