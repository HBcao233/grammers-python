use pyo3::{Py, PyAny, PyResult, Python};
use pyo3_async_runtimes::into_future_with_locals;
use pyo3_async_runtimes::tokio::get_current_locals;
use pyo3_async_runtimes::tokio::future_into_py_with_locals;

pub async fn into_future(coro: Py<PyAny>) -> PyResult<Py<PyAny>> {
    let future =
        Python::attach(|py| into_future_with_locals(&get_current_locals(py)?, coro.into_bound(py)))?;
    future.await
}

pub fn future_into_py<'py, F, R>(py: Python<'py>, fut: F) -> PyResult<Bound<'py, PyAny>>
where
    F: Future<Output = R> + Send + 'static,
{
    let locals = get_current_locals(py)?;

    future_into_py_with_locals(
        py,
        locals.clone(),
        scope(locals, fut)
    )
}
