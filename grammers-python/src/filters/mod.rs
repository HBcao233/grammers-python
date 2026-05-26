mod filters;

pub use filters::{PyAndFilter, PyFilter, PyInvertFilter, PyOrFilter, PyXorFilter};

#[pyo3::pymodule(name = "filters")]
pub(crate) mod filters_ {
    #[pymodule_export]
    pub use super::PyFilter;

    #[pymodule_export]
    pub use super::PyInvertFilter;

    #[pymodule_export]
    pub use super::PyAndFilter;

    #[pymodule_export]
    pub use super::PyOrFilter;

    #[pymodule_export]
    pub use super::PyXorFilter;
}
