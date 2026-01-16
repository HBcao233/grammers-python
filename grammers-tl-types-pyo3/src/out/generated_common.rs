use pyo3::{Python, Py};
use pyo3::{FromPyObject, IntoPyObject};

#[derive(Debug, FromPyObject)]
pub enum PyTLRequest {
    Ping(pyo3::Py<crate::functions::PyPing>),
}
impl grammers_tl_types::Serializable for PyTLRequest {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        match self {
            Self::Ping(x) => Python::attach(|py| {
                x.borrow(py).serialize(buf)
            }),
        }
    }
}
impl grammers_tl_types::RemoteCall for PyTLRequest {
    type Return = crate::PyTLObject;
}

#[derive(Debug, IntoPyObject)]
pub enum PyTLObject {
    Pong(Py<crate::types::PyPong>),
}
impl grammers_tl_types::Deserializable for PyTLObject {
    fn deserialize(buf: crate::Buffer) -> grammers_tl_types::deserialize::Result<Self> {
        use grammers_tl_types::Identifiable;
        let id = u32::deserialize(buf)?;
        Ok(match id {
            crate::types::PyPong::CONSTRUCTOR_ID => Self::Pong(
                pyo3::Python::attach(|py| {
                    let x = crate::types::PyPong::deserialize(buf)?;
                    let init = pyo3::PyClassInitializer::from(crate::TLObject {})
                        .add_subclass(x);
                    Ok(pyo3::Py::new(py, init).expect("init"))
                })?
            ),
            _ => return Err(grammers_tl_types::deserialize::Error::UnexpectedConstructor { id }),
        })
    }
}
