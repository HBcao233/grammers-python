use pyo3::PyResult;

use super::{User, Group, Channel};

use grammers_session_pyo3::{PyPeerAuth, PyPeerId, PyPeerInfo, PyPeerRef};
use grammers_tl_types as tl;
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
#[derive(Clone, Debug)]
pub enum Peer {
    /// A [`User`].
    User(User),

    /// A [`Group`] chat.
    Group(Group),

    /// A broadcast [`Channel`].
    Channel(Channel),
}

impl Peer {
    pub(crate) fn from_user(client: &PyClient, user: tl::enums::User) -> Self {
        Self::User(User::from_raw(client, user))
    }

    pub fn from_raw(client: &PyClient, chat: tl::enums::Chat) -> Self {
        use tl::enums::Chat as C;

        match chat {
            C::Empty(_) | C::Chat(_) | C::Forbidden(_) => {
                Self::Group(Group::from_raw(client, chat))
            }
            C::Channel(ref channel) => {
                if channel.broadcast {
                    Self::Channel(Channel::from_raw(client, chat))
                } else {
                    Self::Group(Group::from_raw(client, chat))
                }
            }
            C::ChannelForbidden(ref channel) => {
                if channel.broadcast {
                    Self::Channel(Channel::from_raw(client, chat))
                } else {
                    Self::Group(Group::from_raw(client, chat))
                }
            }
        }
    }

    /// Return the unique identifier for this peer.
    ///
    /// Every account will see the same identifier for the same peer.
    ///
    /// This identifier will never change. However, small group chats may be migrated to
    /// megagroups. If this happens, both the old small group chat and the new megagroup
    /// exist as separate chats with different identifiers, but they are linked with a
    /// property.
    pub fn id(&self) -> PyPeerId {
        match self {
            Self::User(user) => user.id(),
            Self::Group(group) => group.id(),
            Self::Channel(channel) => channel.id(),
        }
    }

    /// Non-min auth stored in the peer, if any.
    pub(crate) fn auth(&self) -> Option<PyPeerAuth> {
        match self {
            Self::User(user) => user.auth(),
            Self::Group(group) => group.auth(),
            Self::Channel(channel) => channel.auth(),
        }
    }

    /// Convert the peer to its reference.
    ///
    /// This is only possible if the peer would be usable on all methods or if it is in the session cache.
    pub async fn to_ref(&self) -> PyResult<Option<PyPeerRef>> {
        match self {
            Self::User(user) => user.to_ref().await,
            Self::Group(group) => group.to_ref().await,
            Self::Channel(channel) => channel.to_ref().await,
        }
    }

    /// Return the name of this peer.
    ///
    /// For private conversations (users), this is their first name. For groups and channels,
    /// this is their title.
    ///
    /// The name will be `None` if the peer is inaccessible or if the account was deleted. It may
    /// also be `None` if you received it previously.
    pub fn name(&self) -> Option<&str> {
        match self {
            Self::User(user) => user.first_name(),
            Self::Group(group) => group.title(),
            Self::Channel(channel) => Some(channel.title()),
        }
    }

    /// Return the public @username of this peer, if any.
    ///
    /// The returned username does not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of Telegram's URLs, such
    /// as https://t.me/username.
    pub fn username(&self) -> Option<&str> {
        match self {
            Self::User(user) => user.username(),
            Self::Group(group) => group.username(),
            Self::Channel(channel) => channel.username(),
        }
    }

    /// Return collectible usernames of this peer, if any.
    ///
    /// The returned usernames do not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of its username, such
    /// as https://t.me/username.
    pub fn usernames(&self) -> Vec<&str> {
        match self {
            Self::User(user) => user.usernames(),
            Self::Group(group) => group.usernames(),
            Self::Channel(channel) => channel.usernames(),
        }
    }

    // Return the profile picture or chat photo of this peer, if any.
    //
    // This does not fetch the photo, but it may query the session to fetch the peer information.
    /*pub async fn photo(&self, big: bool) -> Option<ChatPhoto> {
        let peer = self.to_ref().await?.into();
        match self {
            Self::User(user) => user.photo().map(|x| ChatPhoto {
                raw: tl::enums::InputFileLocation::InputPeerPhotoFileLocation(
                    tl::types::InputPeerPhotoFileLocation {
                        big,
                        peer,
                        photo_id: x.photo_id,
                    },
                ),
            }),
            Self::Group(group) => group.photo().map(|x| ChatPhoto {
                raw: tl::enums::InputFileLocation::InputPeerPhotoFileLocation(
                    tl::types::InputPeerPhotoFileLocation {
                        big,
                        peer,
                        photo_id: x.photo_id,
                    },
                ),
            }),
            Self::Channel(channel) => channel.photo().map(|x| ChatPhoto {
                raw: tl::enums::InputFileLocation::InputPeerPhotoFileLocation(
                    tl::types::InputPeerPhotoFileLocation {
                        big,
                        peer,
                        photo_id: x.photo_id,
                    },
                ),
            }),
        }
    }*/
}

impl From<Peer> for PyPeerInfo {
    #[inline]
    fn from(peer: Peer) -> Self {
        <Self as From<&Peer>>::from(&peer)
    }
}
impl<'a> From<&'a Peer> for PyPeerInfo {
    fn from(peer: &'a Peer) -> Self {
        match peer {
            Peer::User(user) => <PyPeerInfo as From<&'a User>>::from(user),
            Peer::Group(group) => <PyPeerInfo as From<&'a Group>>::from(group),
            Peer::Channel(channel) => <PyPeerInfo as From<&'a Channel>>::from(channel),
        }
    }
}
