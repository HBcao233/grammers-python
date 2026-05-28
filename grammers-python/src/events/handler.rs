use pyo3::exceptions::{PyException, PyRuntimeError};
use pyo3::prelude::*;
use std::{
    collections::HashMap,
    sync::{Arc, Mutex},
};
use tokio::sync::Semaphore;

use super::{Event, EventBuilder, PyEventKind};
use crate::utils::maybe_await;
use grammers_session_pyo3::into_future;

const HANDLER_PARALLEL_LIMIT: usize = 64;

#[pyclass(name = "HandlerNotFoundError", module = "grammers.event", extends = PyException)]
pub struct PyHandlerNotFoundError {
    #[pyo3(get)]
    pub event_kind: PyEventKind,
}

impl PyHandlerNotFoundError {
    pub fn new_err(event_kind: PyEventKind) -> PyErr {
        PyErr::new::<PyHandlerNotFoundError, _>((event_kind,))
    }
}

#[pymethods]
impl PyHandlerNotFoundError {
    #[new]
    #[pyo3(signature = (event_kind))]
    fn new(event_kind: PyEventKind) -> Self {
        Self { event_kind }
    }

    fn __str__(&self) -> PyResult<String> {
        let kind = self.event_kind.__str__();
        Ok(format!("Event handler of {} is not found.", kind))
    }

    fn __repr__(&self) -> PyResult<String> {
        let kind = self.event_kind.__str__();
        Ok(format!("HandlerNotFoundError(event_kind={})", kind))
    }
}

#[pyclass(name = "EventHandler")]
pub struct PyEventHandler {
    event_builer: EventBuilder,
    handler: Py<PyAny>,
}

#[pymethods]
impl PyEventHandler {
    #[new]
    pub fn new(event_builer: EventBuilder, handler: Py<PyAny>) -> Self {
        Self {
            event_builer,
            handler,
        }
    }

    async fn trigger(&self, event: Py<PyAny>) -> PyResult<()> {
        let need_trigger = match &self.event_builer.filter {
            None => true,
            Some(filter) => {
                let need_trigger = Python::attach(|py| filter.call1(py, (&event,)))?;
                let need_trigger = maybe_await(need_trigger).await?;
                Python::attach(|py| need_trigger.extract(py))?
            }
        };

        if need_trigger {
            let py_handler =
                Python::attach(|py| self.handler.clone_ref(py).call1(py, (event.clone_ref(py),)))?;
            into_future(py_handler).await?;
        }

        Ok(())
    }
}

pub struct EventHandlersManager {
    handlers: Arc<Mutex<HashMap<PyEventKind, Vec<Py<PyEventHandler>>>>>,
    semaphore: Arc<Semaphore>,
}

impl EventHandlersManager {
    pub fn new() -> Self {
        Self {
            handlers: Arc::new(Mutex::new(HashMap::new())),
            semaphore: Arc::new(Semaphore::new(HANDLER_PARALLEL_LIMIT)),
        }
    }

    pub fn add_handler(
        &self,
        py: Python<'_>,
        event_builer: EventBuilder,
        handler: Py<PyAny>,
    ) -> PyResult<()> {
        self.handlers
            .clone()
            .lock()
            .unwrap()
            .entry(event_builer.kind)
            .or_default()
            .push(Py::new(py, PyEventHandler::new(event_builer, handler))?);
        Ok(())
    }

    pub fn trigger_event(&self, event: Event) -> PyResult<()> {
        let kind = event.kind();
        match self.handlers.clone().lock().unwrap().get(&kind) {
            Some(handlers) => {
                if handlers.is_empty() {
                    return Ok(());
                }

                Python::attach(|py| {
                    let client = event.client(py)?.borrow(py).clone();
                    let guard = client.inner.event_pool_handle.lock().unwrap();
                    if guard.is_none() {
                        return Err(PyRuntimeError::new_err("event pool is not running."));
                    }
                    for handler in handlers {
                        let semaphore = self.semaphore.clone();
                        let coro = handler
                            .bind(py)
                            .call_method1("trigger", (event.clone_ref(py),))?
                            .unbind();
                        let _success = guard.as_ref().unwrap().task(Box::pin(async move {
                            let _permit = semaphore.acquire_owned().await.unwrap();
                            into_future(coro).await?;
                            Ok(())
                        }));
                    }

                    Ok(())
                })
            }
            None => Err(PyHandlerNotFoundError::new_err(kind)),
        }
    }
}
