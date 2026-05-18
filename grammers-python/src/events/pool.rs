use std::ops::ControlFlow;

use tokio::sync::mpsc;

use crate::client::{PyClient, UpdateStream};

enum Request {
    Quit,
}

pub struct EventPool {
    handle: EventsPoolHandle,
    runner: EventsPoolRunner,
}

impl EventPool {
    pub fn new(client: &PyClient, updates: UpdateStream) -> Self {
        let (request_tx, request_rx) = mpsc::unbounded_channel();
        Self {
            handle: EventsPoolHandle(request_tx),
            runner: EventsPoolRunner {
                updates,
                client: client.clone(),
            },
        }
    }
}

pub struct EventsPoolHandle(mpsc::UnboundedSender<Request>);

impl EventsPoolHandle {
    pub fn quit(&self) -> bool {
        self.0.send(Request::Quit).is_ok()
    }
}

pub struct EventsPoolRunner {
    updates: UpdateStream,
    client: PyClient,
}

impl EventsPoolRunner {
    pub async fn run(mut self) {
        loop {
            // Empty finished handlers
            while let Some(_) = self.client.event_handlers.tasks.try_join_next() {}
    
            // This code uses `select` on Ctrl+C to gracefully stop the client and have a chance to
            // save the session. You could have fancier logic to save the session if you wanted to
            // (or even save it on every update). Or you could also ignore Ctrl+C and just use
            // `let update = client.next_update().await?`.
            tokio::select! {
                biased;
                (update, state, peers) = self.updates.next_raw()? => {
                    self.client.trigger_event(Event::raw_update(self.client.clone(), update));
                },
                request = self.request_rx.recv() => {
                    let flow = if let Some(request) = request {
                        self.process_request(request).await
                    } else {
                        ControlFlow::Break(())
                    };
                    match flow {
                        ControlFlow::Continue(_) => continue,
                        ControlFlow::Break(_) => break,
                    }
                }
            }
        }
    }
    
    async fn process_request(request: &Request) -> ControlFlow<()> {
        match request {
            Request::Quit => ControlFlow::Break(()),
        }
    }
}
