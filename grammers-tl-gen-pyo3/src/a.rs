    // ======== Chat Attribute ========

    #[pyo3(get, set)]
    pub deactivated: bool,
    #[pyo3(get, set)]
    pub call_active: bool,
    #[pyo3(get, set)]
    pub call_not_empty: bool,
    #[pyo3(get, set)]
    pub noforwards: bool,

    pub participants_count: i32,

    pub date: i32,
    #[pyo3(get, set)]
    pub version: i32,
    #[pyo3(get, set)]
    pub migrated_to: Option<crate::enums::PyInputChannel>,
    #[pyo3(get, set)]
    pub admin_rights: Option<crate::enums::PyChatAdminRights>,
    #[pyo3(get, set)]
    pub default_banned_rights: Option<crate::enums::PyChatBannedRights>,
    
    // ======== Channel Attribute ========

    #[pyo3(get, set)]
    pub verified: bool,

    #[pyo3(get, set)]
    pub restricted: bool,
    #[pyo3(get, set)]
    pub signatures: bool,
    #[pyo3(get, set)]
    pub min: bool,
    #[pyo3(get, set)]
    pub scam: bool,
    #[pyo3(get, set)]
    pub has_link: bool,
    #[pyo3(get, set)]
    pub has_geo: bool,
    #[pyo3(get, set)]
    pub slowmode_enabled: bool,
    #[pyo3(get, set)]
    pub call_active: bool,
    #[pyo3(get, set)]
    pub call_not_empty: bool,
    #[pyo3(get, set)]
    pub fake: bool,

    #[pyo3(get, set)]
    pub noforwards: bool,
    #[pyo3(get, set)]
    pub join_to_send: bool,
    #[pyo3(get, set)]
    pub join_request: bool,
    #[pyo3(get, set)]
    pub forum: bool,
    #[pyo3(get, set)]
    pub stories_hidden: bool,
    #[pyo3(get, set)]
    pub stories_hidden_min: bool,
    #[pyo3(get, set)]
    pub stories_unavailable: bool,
    #[pyo3(get, set)]
    pub signature_profiles: bool,
    #[pyo3(get, set)]
    pub autotranslation: bool,
    #[pyo3(get, set)]
    pub broadcast_messages_allowed: bool,
    #[pyo3(get, set)]
    pub monoforum: bool,
    #[pyo3(get, set)]
    pub forum_tabs: bool,

    #[pyo3(get, set)]
    pub access_hash: Option<i64>,

#[pyo3(get, set)]
    pub date: i32,
    #[pyo3(get, set)]
    pub restriction_reason: Option<Vec<crate::enums::PyRestrictionReason>>,
    #[pyo3(get, set)]
    pub admin_rights: Option<crate::enums::PyChatAdminRights>,
    #[pyo3(get, set)]
    pub banned_rights: Option<crate::enums::PyChatBannedRights>,
    #[pyo3(get, set)]
    pub default_banned_rights: Option<crate::enums::PyChatBannedRights>,
    #[pyo3(get, set)]
    pub participants_count: Option<i32>,
    #[pyo3(get, set)]
    pub usernames: Option<Vec<crate::enums::PyUsername>>,
    #[pyo3(get, set)]
    pub stories_max_id: Option<crate::enums::PyRecentStory>,
    #[pyo3(get, set)]
    pub color: Option<crate::enums::PyPeerColor>,
    #[pyo3(get, set)]
    pub profile_color: Option<crate::enums::PyPeerColor>,
    #[pyo3(get, set)]
    pub emoji_status: Option<crate::enums::PyEmojiStatus>,
    #[pyo3(get, set)]
    pub level: Option<i32>,
    #[pyo3(get, set)]
    pub subscription_until_date: Option<i32>,
    #[pyo3(get, set)]
    pub bot_verification_icon: Option<i64>,
    #[pyo3(get, set)]
    pub send_paid_messages_stars: Option<i64>,
    #[pyo3(get, set)]
    pub linked_monoforum_id: Option<i64>,
    