use pyo3::prelude::*;

use grammers_session_pyo3::{PeerInfo, PyPeerAuth, PyPeerId, PyPeerRef};
use grammers_tl_types as tl;

use super::{PyChannel, PyGroup, PyUser};
use crate::PyClient;
// use crate::media::ChatPhoto;

/// A user, group, or broadcast channel.
///
/// Peers represent places where you can initiate a message exchange with others.
/// After doing so, user accounts can retrieve them via their [`Dialog`] list.
///
/// * Private conversations with other people are treated as the peer of the user itself.
/// * Conversations in a group, whether it's private or public, are simply known as groups.
/// * Conversations where only administrators broadcast messages are known as channels.
#[derive(Debug, FromPyObject, IntoPyObject)]
pub enum PyPeer {
    /// A [`User`].
    User(Py<PyUser>),

    /// A [`Group`] chat.
    Group(Py<PyGroup>),

    /// A broadcast [`Channel`].
    Channel(Py<PyChannel>),
}
impl Clone for PyPeer {
    fn clone(&self) -> Self {
        Python::attach(|py| match self {
            Self::User(x) => Self::User(Py::clone_ref(x, py)),
            Self::Group(x) => Self::Group(Py::clone_ref(x, py)),
            Self::Channel(x) => Self::Channel(Py::clone_ref(x, py)),
        })
    }
}

impl PyPeer {
    pub(crate) fn from_user(client: &PyClient, user: tl::enums::User) -> PyResult<Self> {
        Ok(Self::User(Python::attach(|py| {
            Py::new(py, PyUser::from_raw(client, user))
        })?))
    }

    pub fn from_chat(client: &PyClient, chat: tl::enums::Chat) -> PyResult<Self> {
        use tl::enums::Chat as C;

        Python::attach(|py| {
            Ok(match chat {
                C::Empty(_) | C::Chat(_) | C::Forbidden(_) => {
                    Self::Group(Py::new(py, PyGroup::from_raw(client, chat)?)?)
                }
                C::Channel(ref channel) => {
                    if channel.broadcast {
                        Self::Channel(Py::new(py, PyChannel::from_raw(client, chat)?)?)
                    } else {
                        Self::Group(Py::new(py, PyGroup::from_raw(client, chat)?)?)
                    }
                }
                C::ChannelForbidden(ref channel) => {
                    if channel.broadcast {
                        Self::Channel(Py::new(py, PyChannel::from_raw(client, chat)?)?)
                    } else {
                        Self::Group(Py::new(py, PyGroup::from_raw(client, chat)?)?)
                    }
                }
            })
        })
    }

    pub fn id(&self) -> PyPeerId {
        Python::attach(|py| match self {
            Self::User(x) => x.borrow(py).id(),
            Self::Group(x) => x.borrow(py).id(),
            Self::Channel(x) => x.borrow(py).id(),
        })
    }

    pub fn auth(&self) -> Option<PyPeerAuth> {
        Python::attach(|py| match self {
            Self::User(x) => x.borrow(py).auth(),
            Self::Group(x) => x.borrow(py).auth(),
            Self::Channel(x) => x.borrow(py).auth(),
        })
    }

    pub async fn to_ref(&self) -> PyResult<Option<PyPeerRef>> {
        Ok(match self {
            Self::User(x) => {
                let (id, auth, session) = Python::attach(|py| {
                    let borrowed = x.borrow(py);
                    (borrowed.id(), borrowed.auth(), borrowed.client.session())
                });
                match auth {
                    Some(auth) => Some(PyPeerRef { id, auth }),
                    None => session.peer_ref(id).await?,
                }
            }
            Self::Group(x) => {
                let (id, auth, session) = Python::attach(|py| {
                    let borrowed = x.borrow(py);
                    (borrowed.id(), borrowed.auth(), borrowed.client.session())
                });
                match auth {
                    Some(auth) => Some(PyPeerRef { id, auth }),
                    None => session.peer_ref(id).await?,
                }
            }
            Self::Channel(x) => {
                let (id, auth, session) = Python::attach(|py| {
                    let borrowed = x.borrow(py);
                    (borrowed.id(), borrowed.auth(), borrowed.client.session())
                });
                match auth {
                    Some(auth) => Some(PyPeerRef { id, auth }),
                    None => session.peer_ref(id).await?,
                }
            }
        })
    }

    pub fn info(&self) -> PeerInfo {
        Python::attach(|py| match self {
            Self::User(x) => x.borrow(py).info(),
            Self::Group(x) => x.borrow(py).info(),
            Self::Channel(x) => x.borrow(py).info(),
        })
    }
}
