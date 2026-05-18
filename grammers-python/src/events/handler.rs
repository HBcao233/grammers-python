use std::{
    collections::HashMap,
    sync::Mutex,
};
use tokio::task::JoinSet;

use super::{EventKind, EventBuilder};
use crate::utils::maybe_await;
use grammers_session_pyo3::into_future;

pub(crate) struct EventHandler {
    event_builer: EventBuiler,
    handler: Py<PyAny>,
}

impl EventHandler {
    pub fn new(event_builer: EventBuiler, handler: Py<PyAny>) -> Self {
        Self {
            event_builer,
            handler,
        }
    }
}

pub(crate) struct EventHandlersManager {
    handlers: Mutex<HashMap<EventKind, Vec<EventHandler>>>,
    tasks: JoinSet<()>,
}

impl EventHandlersManager {
    pub fn new() -> Self {
        Self {
            handlers: Mutex::new(HashMap::new()),
        }
    }
    
    pub fn add_handler(&self, event_builer: EventBuiler, handler: Py<PyAny>) {
        self.handlers
            .lock()
            .unwrap()
            .entry(event_builer.kind)
            .or_default()
            .push(EventHandler::new(event_builer, handler));
    }
    
    pub fn trigger_event(&self, event: Event) -> PyResult<()> {
        let kind = event.kind();
        let client = Python::attach(|py| event.client());
        match self.handlers.lock().unwrap().get(&kind) {
            Some(handlers) => Python::attach(|py| {
                for handler in handlers {
                    self.tasks.spawn(async move {
                        let result = async move {
                            let need_trigger = handler.event_builer.call1((event.clone_ref(py),))?;
                            let need_trigger = maybe_await(need_trigger).await?;
                            let need_trigger: bool = need_trigger.extract()?;
                            
                            let handler = handler.handler.call1((event.clone_ref(py),))?;
                            into_future(handler).map(|_| ())
                        }.await;
                        
                        match kind {
                            // If current event is ErrorEvent directly panic, to avoid recursion.
                            PyEventKind::Error => {
                                eprintln!("FATAL: Error handler logic error! Program terminated.");
                                Python::attach(|py| {
                                    err.print(py);
                                });
                            },
                            // trigger ErrorEvent
                            _ => {
                                if let Err(err) = result {
                                    self.trigger_event(Event::error(client.clone(), err));
                                }
                            },
                        }
                    })
                }
            }),
            None => Err(PyKeyError:new_err(format!("'{}'", kind.__str__()))),
        }
    }
}
