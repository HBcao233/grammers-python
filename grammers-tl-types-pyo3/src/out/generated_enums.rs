pub mod enums {
    pub enum PyPoll {
        Poll(crate::types::PyPoll),
    }
    impl From<crate::types::PyPoll> for PyPoll {
        fn from(x: crate::types::PyPoll) -> Self {
            Self::Poll(x)
        }
    }
}