use pyo3::exceptions::PyRuntimeError;
use pyo3::{Py, PyResult, Python};
use std::ops::ControlFlow;
use std::pin::Pin;
use tokio::sync::mpsc;
use tokio::task::JoinSet;

use super::Event;
use crate::client::{PyClient, UpdateStream};

enum Request {
    Task {
        fut: Pin<Box<dyn Future<Output = PyResult<()>> + Send + 'static>>,
    },
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
                tasks: JoinSet::new(),
            },
        }
    }
}

pub struct EventPoolHandle(mpsc::UnboundedSender<Request>);

impl EventPoolHandle {
    pub fn task(&self, fut: Pin<Box<dyn Future<Output = PyResult<()>> + Send + 'static>>) -> bool {
        self.0.send(Request::Task { fut }).is_ok()
    }

    pub fn quit(&self) -> bool {
        self.0.send(Request::Quit).is_ok()
    }
}

pub struct EventPoolRunner {
    updates: UpdateStream,
    request_rx: mpsc::UnboundedReceiver<Request>,
    client: Py<PyClient>,
    tasks: JoinSet<PyResult<()>>,
}

impl EventPoolRunner {
    pub async fn run(mut self) -> PyResult<()> {
        let client = Python::attach(|py| self.client.borrow(py).clone());

        let res = loop {
            tokio::select! {
                biased;
                Ok((update, _state, _peers)) = self.updates.next_raw() => {
                    let event = match Python::attach(|py| Event::raw_update(py, self.client.clone_ref(py), update.into())) {
                        Ok(event) => event,
                        Err(e) => break Err(e),
                    };

                    if let Err(e) = client.trigger_event(event) {
                        break Err(e);
                    }
                },
                Some(task_result) = self.tasks.join_next(), if !self.tasks.is_empty() => {
                    match task_result {
                        Err(e) => break Err(PyRuntimeError::new_err(format!("JoinHandle fail {:?}", e))),
                        Ok(res) => {
                            if let Err(e) = res {
                                break Err(e);
                            }
                        }
                    }
                },
                request = self.request_rx.recv() => {
                    let flow = if let Some(request) = request {
                        self.process_request(request).await
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

        // Signal anyone waiting on idle() that the event pool has finished.
        let inner = Python::attach(|py| self.client.borrow(py).inner.clone());
        inner.event_pool_done.notify_waiters();

        res
    }

    async fn process_request(&mut self, request: Request) -> ControlFlow<()> {
        match request {
            Request::Task { fut } => {
                self.tasks.spawn(async move { fut.await });
                ControlFlow::Continue(())
            }
            Request::Quit => ControlFlow::Break(()),
        }
    }
}
