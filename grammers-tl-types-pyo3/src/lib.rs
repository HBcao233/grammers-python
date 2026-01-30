mod common;
mod generated;
pub mod utils;

pub use common::{
    PyRawVec_enums_AccessPointRule, PyRawVec_enums_IpPort, PyRawVec_enums_TlsBlock,
    PyRawVec_types_FutureSalt, PyTLObjectWrapper, PyTLRequestWrapper, TLObject, TLRequest,
};
pub use generated::{PyTLObject, PyTLRequest, enums, functions, types};
use generated::{functions_, types_};

use grammers_tl_types::deserialize::Cursor;

pub type Buffer<'a, 'b> = &'a mut Cursor<'b>;

#[pyo3::pymodule(name = "tl", module = "grammers")]
pub mod tl {
    #[pymodule_export]
    use crate::TLObject;

    #[pymodule_export]
    use crate::TLRequest;

    #[pymodule_export]
    use crate::types_;

    #[pymodule_export]
    use crate::functions_;
}
