pub mod functions {
    #[derive(Debug, Clone)]
    #[pyo3::pyclass(name = "Ping", extends = crate::TLRequest)]
    pub struct PyPing {
        #[pyo3(get, set)]
        pub ping_id: i64,
    }
    #[pyo3::pymethods]
    impl PyPing {
        #[new]
        fn new(
            ping_id: i64,
        ) -> (Self, crate::TLRequest) {
            (Self {
                ping_id,
            }, 
            crate::TLRequest {})
        }
    }
    impl grammers_tl_types::Identifiable for PyPing {
        const CONSTRUCTOR_ID: u32 = 2059302892;
    }
    impl grammers_tl_types::Serializable for PyPing {
        fn serialize(&self, buf: &mut impl Extend<u8>) {
            use grammers_tl_types::Identifiable;
            Self::CONSTRUCTOR_ID.serialize(buf);
            self.ping_id.serialize(buf);
        }
    }
    /*
    impl grammers_tl_types::RemoteCall for PyPing {
        type Return = crate::enums::PyPong;
    }*/
}