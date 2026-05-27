use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::{PyCFunction, PyTuple};
use std::ffi::{CStr, CString};

use crate::PyClient;
use crate::client::UpdatesConfiguration;
use crate::events::{Event, EventBuilder, EventPool};
// use crate::runtime::RUNTIME;
use grammers_tl_types as tl;
use grammers_session_pyo3::{PyUpdatesState, UpdateStateLike};

#[pymethods]
impl PyClient {
    pub fn _is_event_pool_running(&self) -> bool {
        let inner = self.inner.clone();
        inner.event_pool_handle.lock().unwrap().is_some()
    }

    pub async fn _start_event_pool(&self) -> PyResult<()> {
        let inner = self.inner.clone();
        
        // In the extremely rare case where `Err` happens, there's not much we can do.
        // `message_box` will try to correct its state as updates arrive.
        let update_state = self.invoke(&tl::functions::updates::GetState {}).await;
        if let Ok(tl::enums::updates::State::State(state)) = update_state {
            inner
                .session
                .set_update_state(UpdateStateLike::All(PyUpdatesState {
                    pts: state.pts,
                    qts: state.qts,
                    date: state.date,
                    seq: state.seq,
                    channels: Vec::new(),
                }))
                .await?;
        }
        
        let updates = inner
            .updates
            .lock()
            .unwrap()
            .take()
            .ok_or(PyRuntimeError::new_err("Client fail to initialize."))?;
        let update_stream = self
            .stream_updates(
                updates,
                UpdatesConfiguration {
                    catch_up: true,
                    update_queue_limit: Some(100),
                },
            )
            .await?;
        let EventPool { runner, handle } = Python::attach(|py| {
            Ok::<_, PyErr>(EventPool::new(Py::new(py, self.clone())?, update_stream))
        })?;
        let event_pool_task = pyo3_async_runtimes::tokio::get_runtime().spawn(runner.run());

        *inner.event_pool_handle.lock().unwrap() = Some(handle);
        *inner.event_pool_task.lock().unwrap() = Some(event_pool_task);

        Ok(())
    }

    pub async fn _stop_event_pool(&self) -> PyResult<()> {
        let inner = self.inner.clone();

        let event_pool_handle = {
            let mut guard = inner.event_pool_handle.lock().unwrap();
            guard.take()
        };
        match event_pool_handle {
            Some(event_pool_handle) => {
                event_pool_handle.quit();
                let event_pool_task = {
                    let mut guard = inner.event_pool_task.lock().unwrap();
                    guard.take().unwrap()
                };
                let res = event_pool_task
                    .await
                    .map_err(|e| PyRuntimeError::new_err(format!("JoinHandle error: {:?}", e)))?;
                res?;
                Ok(())
            }
            None => return Err(PyRuntimeError::new_err("event pool is not running.")),
        }
    }

    #[pyo3(signature = (event, handler))]
    pub fn add_handler(&self, event: EventBuilder, handler: Py<PyAny>) -> PyResult<()> {
        let is_coro_func: bool = Python::attach(|py| {
            let inspect = crate::utils::inspect(py)?;
            Ok::<bool, PyErr>(
                inspect
                    .bind(py)
                    .call_method1("iscoroutinefunction", (&handler,))?
                    .extract()?,
            )
        })?;
        if !is_coro_func {
            return Err(PyValueError::new_err(
                "handler must be a coroutine function.",
            ));
        }
        Python::attach(|py| self.inner.event_handlers.add_handler(py, event, handler))?;
        Ok(())
    }

    pub fn on(slf: &Bound<'_, Self>, event: EventBuilder) -> PyResult<Py<PyCFunction>> {
        let kind_name = event.kind.name();
        let add_handler = slf.getattr("add_handler")?.unbind();

        let func_name = CString::new(format!("{}EventHandlerWrapper", kind_name))
            .map_err(|_| PyRuntimeError::new_err("CString::new failed"))?;
        let func_name: &'static CStr = Box::leak(func_name.into_boxed_c_str());
        let func_doc = CString::new(format!(
            "Wrapper a function to a {}Event handler",
            kind_name
        ))
        .map_err(|_| PyRuntimeError::new_err("CString::new failed"))?;
        let func_doc: &'static CStr = Box::leak(func_doc.into_boxed_c_str());

        Ok(PyCFunction::new_closure(
            slf.py(),
            Some(func_name),
            Some(func_doc),
            move |args: &Bound<'_, PyTuple>, _| -> PyResult<()> {
                let py = args.py();
                let func = args.get_item(0)?;
                add_handler.call1(py, (event.clone_ref(py), func))?;
                Ok(())
            },
        )?
        .unbind())
    }

    pub fn trigger_event(&self, event: Event) -> PyResult<()> {
        self.inner.event_handlers.trigger_event(event)?;
        Ok(())
    }
}
