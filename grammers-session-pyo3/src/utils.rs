use pyo3::prelude::*;
use pyo3::types::{PyCFunction, PyTuple};
use tokio::sync::oneshot;

/// 在 Tokio spawn 的任务中安全地 await Python coroutine
pub async fn into_future(event_loop: &Py<PyAny>, py_coro: Py<PyAny>) -> PyResult<Py<PyAny>>
{
    let (tx, rx) = oneshot::channel::<PyResult<Py<PyAny>>>();
    
    Python::attach(|py| -> PyResult<()> {
        let asyncio = py.import("asyncio")?;
        let _ = asyncio.call_method1("set_event_loop", (event_loop,))?;
        
        let concurrent_future = asyncio.call_method1(
            "run_coroutine_threadsafe", 
            (py_coro.bind(py), event_loop)
        )?;
        
        let tx = std::sync::Arc::new(std::sync::Mutex::new(Some(tx)));
        
        let callback = PyCFunction::new_closure(
            py,
            None,
            None,
            move |args: &Bound<'_, PyTuple>, _| -> PyResult<()> {
                let fut = args.get_item(0)?;
                let result = fut
                    .call_method0("result").map(|x| x.unbind());
                
                if let Some(tx) = tx.lock().unwrap().take() {
                    let _ = tx.send(result);
                }
                Ok(())
            },
        )?;
        
        concurrent_future.call_method1("add_done_callback", (callback,))?;
        Ok(())
    })?;
    
    rx.await.map_err(|_| {
        PyErr::new::<pyo3::exceptions::PyRuntimeError, _>("Callback channel dropped")
    })?
}
