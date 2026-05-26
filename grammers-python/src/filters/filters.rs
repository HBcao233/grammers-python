use pyo3::exceptions::{PyNotImplementedError, PyTypeError};
use pyo3::prelude::*;

use crate::utils::maybe_await;

#[pyclass(name = "Filter", module = "grammers.filters", subclass, dict)]
pub struct PyFilter {}

#[pymethods]
impl PyFilter {
    #[new]
    fn new() -> Self {
        Self {}
    }

    #[classmethod]
    fn __init_subclass__(cls: &Bound<'_, PyType>) -> PyResult<()> {
        let py = cls.py();
        let cls_dict = cls.getattr("__dict__")?;
        if !cls_dict.contains("__call__")? {
            return Err(PyTypeError::new_err(format!(
                "Can't instantiate abstract class '{}' without an implementation for abstract method '{}'",
                cls.qualname()?,
                method,
            )));
        }

        Ok(())
    }

    fn __invert__(&self) -> PyResult<Py<PyInvertFilter>> {
        Py::new(py, PyInvertFilter::new(self))
    }

    fn __and__(&self, other: Py<PyAny>) -> PyResult<Py<PyAndFilter>> {
        Py::new(py, PyAndFilter::new(self, other))
    }

    fn __or__(&self, other: Py<PyAny>) -> PyResult<Py<PyOrFilter>> {
        Py::new(py, PyOrFilter::new(self, other))
    }

    fn __xor__(&self, other: Py<PyAny>) -> PyResult<Py<PyXorFilter>> {
        Py::new(py, PyXorFilter::new(self, other))
    }

    async fn __call__(&self, event: Py<PyAny>) -> bool {
        Err(PyNotImplementedError::new_err(()))
    }
}

#[pyclass(name = "InvertFilter", module = "grammers.filters", extends = PyFilter)]
pub struct PyInvertFilter {
    base: Py<PyAny>,
}

#[pymethods]
impl PyInvertFilter {
    #[new]
    pub fn new(base: Py<PyAny>) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyFilter {}).add_subclass(Self { base })
    }

    async fn __call__(&self, event: Py<PyAny>) -> bool {
        let base = Python::attach(|py| self.base.bind(py).call1((event,)))?;
        let x = maybe_await(base).await?;
        let x = Python::attach(|py| x.bind(py).extract::<bool>())?;
        !x
    }
}

#[pyclass(name = "AndFilter", module = "grammers.filters", extends = PyFilter)]
pub struct PyAndFilter {
    base: Py<PyAny>,
    other: Py<PyAny>,
}

#[pymethods]
impl PyAndFilter {
    #[new]
    pub fn new(base: Py<PyAny>, other: Py<PyAny>) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyFilter {}).add_subclass(Self { base, other })
    }

    async fn __call__(&self, event: Py<PyAny>) -> bool {
        let base = Python::attach(|py| self.base.bind(py).call1((event,)))?;
        let x = maybe_await(base).await?;
        let x = Python::attach(|py| x.bind(py).extract::<bool>())?;
        if !x {
            return false;
        }

        let other = Python::attach(|py| self.other.bind(py).call1((event,)))?;
        let y = maybe_await(other).await?;
        let y = Python::attach(|py| y.bind(py).extract::<bool>())?;

        x && y
    }
}

#[pyclass(name = "OrFilter", module = "grammers.filters", extends = PyFilter)]
pub struct PyOrFilter {
    base: Py<PyAny>,
    other: Py<PyAny>,
}

#[pymethods]
impl PyOrFilter {
    #[new]
    pub fn new(base: Py<PyAny>, other: Py<PyAny>) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyFilter {}).add_subclass(Self { base, other })
    }

    async fn __call__(&self, event: Py<PyAny>) -> bool {
        let base = Python::attach(|py| self.base.bind(py).call1((event,)))?;
        let x = maybe_await(base).await?;
        let x = Python::attach(|py| x.bind(py).extract::<bool>())?;
        if x {
            return true;
        }

        let other = Python::attach(|py| self.other.bind(py).call1((event,)))?;
        let y = maybe_await(other).await?;
        let y = Python::attach(|py| y.bind(py).extract::<bool>())?;

        x || y
    }
}

#[pyclass(name = "XorFilter", module = "grammers.filters", extends = PyFilter)]
pub struct PyXorFilter {
    base: Py<PyAny>,
    other: Py<PyAny>,
}

#[pymethods]
impl PyXorFilter {
    #[new]
    pub fn new(base: Py<PyAny>, other: Py<PyAny>) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyFilter {}).add_subclass(Self { base, other })
    }

    async fn __call__(&self, event: Py<PyAny>) -> bool {
        let base = Python::attach(|py| self.base.bind(py).call1((event,)))?;
        let x = maybe_await(base).await?;
        let x = Python::attach(|py| x.bind(py).extract::<bool>())?;

        let other = Python::attach(|py| self.other.bind(py).call1((event,)))?;
        let y = maybe_await(other).await?;
        let y = Python::attach(|py| y.bind(py).extract::<bool>())?;

        x ^ y
    }
}
