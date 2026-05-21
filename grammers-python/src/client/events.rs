use pyo3::prelude::*;

use crate::PyClient;
use crate::events::EventBuilder;

#[pymethods]
impl PyClient {
    #[pyo3(signature = (event, handler))]
    pub fn add_handler(&self, event: EventBuilder, handler: Py<PyAny>) -> PyResult<()> {
        self.event_handlers.add_handler(event, handler);
        Ok(())
    }

    pub fn on(slf: Bound<'_, Self>, event: EventBuilder) -> PyCFunction {
        let kind_name = event.kind.name();
        let add_handler = slf.getattr("add_handler")?;
        PyCFunction::new_closure(
            slf.py(),
            format!("{}EventHandlerWrapper", kind_name),
            format!("Wrapper a function to a {}Event handler", kind_name),
            move |args: &Bound<'_, PyTuple>, _| -> PyResult<()> {
                let py = args.py();
                let func = args.get_item(0)?;
                add_handler.call1((event, func))?;
                Ok(())
            },
        )
    }

    pub fn trigger_event(event: Event) -> PyResult<()> {
        self.event_handlers.trigger_event(event)
    }
}
