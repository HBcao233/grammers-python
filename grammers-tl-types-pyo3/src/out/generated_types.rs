pub mod types {
    #[derive(Debug, Clone)]
    #[pyo3::pyclass(name = "Pong", extends = crate::TLObject)]
    pub struct PyPong {
        #[pyo3(get, set)]
        pub msg_id: i64,
        #[pyo3(get, set)]
        pub ping_id: i64,
    }
    #[pyo3::pymethods]
    impl PyPong {
        #[new]
        fn new(
            msg_id: i64,
            ping_id: i64,
        ) -> (Self, crate::TLObject) {
            (Self {
                msg_id,
                ping_id,
            }, 
            crate::TLObject {})
        }
        
        fn to_dict(&self) -> pyo3::PyResult<pyo3::Py<pyo3::types::PyDict>> {
            pyo3::Python::attach(|py| {
                use pyo3::types::PyDictMethods;
                let dict = pyo3::types::PyDict::new(py);
                dict.set_item("msg_id", self.msg_id)?;
                dict.set_item("ping_id", self.ping_id)?;
                Ok(dict.into())
            })
        }
    }
    impl grammers_tl_types::Identifiable for PyPong {
        const CONSTRUCTOR_ID: u32 = 880243653;
    }
    /*impl grammers_tl_types::Serializable for PyPong {
        fn serialize(&self, buf: &mut impl Extend<u8>) {
            self.msg_id.serialize(buf);
            self.ping_id.serialize(buf);
        }
    }*/
    impl grammers_tl_types::Deserializable for PyPong {
        fn deserialize(buf: crate::Buffer) -> grammers_tl_types::deserialize::Result<Self> {
            let msg_id = i64::deserialize(buf)?;
            let ping_id = i64::deserialize(buf)?;
            Ok(PyPong {
                msg_id,
                ping_id,
            })
        }
    }
    /*
    impl From<crate::enums::PyPong> for PyPong {
        fn from(x: crate::enums::PyPong) -> Self {
            match x {
                crate::enums::PyPong::Pong(x) => pyo3::Python::attach(|py| x.extract(py).expect("xx")),
            }
        }
    }*/
}