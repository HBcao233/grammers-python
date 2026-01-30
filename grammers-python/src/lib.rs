//! grammers-python: Python bindings for the grammers Telegram client library
//!
//! 提供 grammers 各个组件的 Python 绑定

mod client;
mod crypto;
mod errors;
mod peer;
mod utils;

use client::{PyClient, PyLoginToken};

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
    use super::crypto::_crypto;

    #[pymodule_export]
    use super::errors::_errors;

    #[pymodule_export]
    use grammers_tl_types_pyo3::tl;

    #[pymodule_export]
    use grammers_session_pyo3::sessions_;

    #[pymodule_export]
    use super::PyLoginToken;

    #[pymodule_export]
    use super::PyClient;

    #[pymodule_init]
    fn init(_m: &Bound<'_, PyModule>) -> PyResult<()> {
        // pyo3_asyncio::tokio::init_multi_thread();
        pyo3_log::init();
        Ok(())
    }
}
