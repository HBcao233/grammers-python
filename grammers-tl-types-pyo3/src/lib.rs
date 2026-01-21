mod serialize;
pub mod deserialize;
mod common;
mod generated;

pub use common::{Identifiable, PyRawVec, PyTLObjectWrapper, PyTLRequestWrapper, TLObject, TLRequest};
pub use generated::{LAYER, name_for_id, PyTLObject, PyTLRequest, enums, functions, types};
use generated::{functions_, types_};

pub use serialize::Serializable;
use deserialize::Buffer;
pub use deserialize::{Cursor, Deserializable};

#[pyo3::pymodule(name = "tl", module = "grammers")]
pub mod tl {
    #[pymodule_export]
    const LAYER: i32 = super::LAYER;
    
    #[pymodule_export]
    use crate::TLObject;

    #[pymodule_export]
    use crate::TLRequest;

    #[pymodule_export]
    use crate::types_;

    #[pymodule_export]
    use crate::functions_;
}
