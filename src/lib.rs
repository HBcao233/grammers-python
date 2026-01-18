//! grammers-python: Python bindings for the grammers Telegram client library
//!
//! 提供 grammers 各个组件的 Python 绑定
mod client;
mod crypto;
pub mod errors;

#[pyo3::pymodule]
mod _rs {
    // use pyo3::prelude::*;

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
    use super::client::PyClient;

    /*
    #[pymodule_init]
    fn init(m: &Bound<'_, PyModule>) -> PyResult<()> {
      // pyo3_asyncio::tokio::init_multi_thread();
      Ok(())
    }*/
}

#[cfg(feature = "stub-gen")]
pyo3_stub_gen::define_stub_info_gatherer!(stub_info);
