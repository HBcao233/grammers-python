use pyo3::prelude::*;

use super::{PyChannel, PyGroup, PyUser};

use crate::PyClient;
use grammers_session_pyo3::{PyPeerAuth, PyPeerId, PyPeerInfo};
use grammers_tl_types as tl;

// use crate::media::ChatPhoto;

/// A user, group, or broadcast channel.
///
/// Peers represent places where you can initiate a message exchange with others.
/// After doing so, user accounts can retrieve them via their [`Dialog`] list.
///
/// * Private conversations with other people are treated as the peer of the user itself.
/// * Conversations in a group, whether it's private or public, are simply known as groups.
/// * Conversations where only administrators broadcast messages are known as channels.
#[derive(IntoPyObject)]
pub enum Peer {
    /// A [`User`].
    User(Py<PyUser>),

    /// A [`Group`] chat.
    Group(Py<PyGroup>),

    /// A broadcast [`Channel`].
    Channel(Py<PyChannel>),
}
impl Clone for Peer {
    fn clone(&self) -> Self {
        Python::attach(|py| match self {
            Self::User(x) => Self::User(x.bind(py).clone().unbind()),
            Self::Group(x) => Self::Group(x.bind(py).clone().unbind()),
            Self::Channel(x) => Self::Channel(x.bind(py).clone().unbind()),
        })
    }
}

impl Peer {
    pub(crate) fn from_user(client: &PyClient, user: tl::enums::User) -> PyResult<Self> {
        Ok(Self::User(Python::attach(|py| 
            Py::new(py, PyUser::from_raw(client, user))
        )?))
    }

    pub fn from_raw(client: &PyClient, chat: tl::enums::Chat) -> PyResult<Self> {
        use tl::enums::Chat as C;

        Python::attach(|py| Ok(match chat {
            C::Empty(_) | C::Chat(_) | C::Forbidden(_) => Self::Group(
                Py::new(py, PyGroup::new(client, chat.into()))?
            ),
            C::Channel(ref channel) => {
                if channel.broadcast {
                    Self::Channel(
                        Py::new(py, PyChannel::new(client, chat.into()))?
                    )
                } else {
                    Self::Group(
                        Py::new(py, PyGroup::new(client, chat.into()))?
                    )
                }
            },
            C::ChannelForbidden(ref channel) => {
                if channel.broadcast {
                    Self::Channel(
                        Py::new(py, PyChannel::new(client, chat.into()))?
                    )
                } else {
                    Self::Group(
                        Py::new(py, PyGroup::new(client, chat.into()))?
                    )
                }
            },
        }))
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
    
    pub fn info(&self) -> PyPeerInfo {
        Python::attach(|py| match self {
            Self::User(x) => x.borrow(py).info(),
            Self::Group(x) => x.borrow(py).info(),
            Self::Channel(x) => x.borrow(py).info(),
        })
    }
}
