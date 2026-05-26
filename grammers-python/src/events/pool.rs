use pyo3::{Py, PyResult, Python};
use std::ops::ControlFlow;
use tokio::sync::mpsc;

use super::Event;
use crate::client::{PyClient, UpdateStream};

enum Request {
    Quit,
}

pub struct EventPool {
    pub handle: EventPoolHandle,
    pub runner: EventPoolRunner,
}

impl EventPool {
    pub fn new(client: Py<PyClient>, updates: UpdateStream) -> Self {
        let (request_tx, request_rx) = mpsc::unbounded_channel();

        Self {
            handle: EventPoolHandle(request_tx),
            runner: EventPoolRunner {
                updates,
                request_rx,
                client,
            },
        }
    }
}

pub struct EventPoolHandle(mpsc::UnboundedSender<Request>);

impl EventPoolHandle {
    pub fn quit(&self) -> bool {
        self.0.send(Request::Quit).is_ok()
    }
}

pub struct EventPoolRunner {
    updates: UpdateStream,
    request_rx: mpsc::UnboundedReceiver<Request>,
    client: Py<PyClient>,
}

impl EventPoolRunner {
    pub async fn run(mut self) -> PyResult<()> {
        let client = Python::attach(|py| self.client.borrow(py).clone());
        let res = loop {
            // Empty finished handlers
            while let Some(_) = client
                .inner
                .event_handlers
                .inner
                .clone()
                .tasks
                .lock()
                .unwrap()
                .try_join_next()
            {}
            
            tokio::select! {
                biased;
                Ok((update, _state, _peers)) = self.updates.next_raw() => {
                    println!("raw_update got");
                    let event = match Python::attach(|py| Event::raw_update(py, self.client.clone_ref(py), update.into())) {
                        Ok(event) => event,
                        Err(e) => break Err(e),
                    };
                    
                    println!("raw_update event created");

                    if let Err(e) = client.trigger_event(event) {
                        break Err(e);
                    }
                    println!("raw_update event trigger");
                },
                request = self.request_rx.recv() => {
                    let flow = if let Some(request) = request {
                        self.process_request(&request).await
                    } else {
                        ControlFlow::Break(())
                    };
                    match flow {
                        ControlFlow::Continue(_) => continue,
                        ControlFlow::Break(_) => break Ok(()),
                    }
                }
            }
        };

        self.updates.sync_update_state().await?;
        res
    }

    async fn process_request(&self, request: &Request) -> ControlFlow<()> {
        match request {
            Request::Quit => ControlFlow::Break(()),
        }
    }
}
