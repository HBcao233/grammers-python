//! grammers-python: Python bindings for the grammers Telegram client library

mod client;
mod crypto;
mod errors;
mod peer;
mod utils;
// mod message;

use client::PyClient;

#[pyo3::pymodule]
mod _rs {
    use pyo3::prelude::*;

    #[pymodule_export]
    #[allow(non_upper_case_globals)]
    const __version__: &str = &env!("CARGO_PKG_VERSION");

    #[pymodule_export]
    #[allow(non_upper_case_globals)]
    const __doc__: &str = &"Python bindings for grammers Telegram client library";

    #[pymodule_export]
    use super::crypto::crypto_;

    #[pymodule_export]
    use super::errors::errors_;

    #[pymodule_export]
    use grammers_tl_types_pyo3::tl;

    #[pymodule_export]
    use grammers_session_pyo3::sessions_;

    #[pymodule_export]
    use super::client::client_;

    #[pymodule_init]
    fn init(_m: &Bound<'_, PyModule>) -> PyResult<()> {
        // pyo3_asyncio::tokio::init_multi_thread();
        pyo3_log::init();
        Ok(())
    }
}
