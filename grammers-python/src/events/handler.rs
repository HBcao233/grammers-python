use pyo3::exceptions::PyKeyError;
use pyo3::{Py, PyAny, PyResult, Python};
use std::{
    collections::HashMap,
    sync::{Arc, Mutex},
};
use tokio::task::JoinSet;

use super::{Event, EventBuilder, PyEventKind};
use crate::utils::maybe_await;
use grammers_session_pyo3::into_future;

pub struct EventHandler {
    event_builer: EventBuilder,
    handler: Py<PyAny>,
}

impl EventHandler {
    pub fn new(event_builer: EventBuilder, handler: Py<PyAny>) -> Self {
        Self {
            event_builer,
            handler,
        }
    }

    pub fn clone_ref(&self, py: Python<'_>) -> Self {
        Self {
            event_builer: self.event_builer.clone_ref(py),
            handler: self.handler.clone_ref(py),
        }
    }
}

pub struct EventHandlersManagerInner {
    handlers: Mutex<HashMap<PyEventKind, Vec<EventHandler>>>,
    pub tasks: Mutex<JoinSet<()>>,
    // error_tx: mpsc::UnboundedSender<PyErr>,
}

#[derive(Clone)]
pub struct EventHandlersManager {
    pub inner: Arc<EventHandlersManagerInner>,
}

impl EventHandlersManager {
    pub fn new() -> Self {
        Self {
            inner: Arc::new(EventHandlersManagerInner {
                handlers: Mutex::new(HashMap::new()),
                tasks: Mutex::new(JoinSet::new()),
            }),
        }
    }

    pub fn add_handler(&self, event_builer: EventBuilder, handler: Py<PyAny>) {
        self.inner
            .handlers
            .lock()
            .unwrap()
            .entry(event_builer.kind)
            .or_default()
            .push(EventHandler::new(event_builer, handler));
    }

    pub fn trigger_event(&self, event: Event) -> PyResult<()> {
        let kind = event.kind();
        let handlers: Vec<EventHandler> =
            match self.inner.clone().handlers.lock().unwrap().get(&kind) {
                Some(handlers) => {
                    Python::attach(|py| handlers.iter().map(|x| x.clone_ref(py)).collect())
                }
                None => return Err(PyKeyError::new_err(format!("'{}'", kind.__str__()))),
            };

        for handler in handlers {
            let manager = self.clone();
            let event_cloned = Python::attach(|py| event.clone_ref(py));

            manager.inner.tasks.lock().unwrap().spawn(async move {
                let result: PyResult<()> = async move {
                    let need_trigger = match &handler.event_builer.filter {
                        None => true,
                        Some(filter) => {
                            let need_trigger = Python::attach(|py| {
                                filter.call1(py, (event_cloned.clone_ref(py),))
                            })?;
                            let need_trigger = maybe_await(need_trigger).await?;
                            Python::attach(|py| need_trigger.extract(py))?
                        }
                    };

                    if need_trigger {
                        let py_handler =
                            Python::attach(|py| handler.handler.call1(py, (event_cloned,)))?;
                        println!("a");
                        into_future(py_handler).await?;
                        println!("b");
                        Ok(())
                    } else {
                        Ok(())
                    }
                }
                .await;

                if let Err(_err) = result {
                    // let _ = manager.inner.error_tx.send(err);
                    todo!();
                }
            });
        }
        Ok(())
    }
}
