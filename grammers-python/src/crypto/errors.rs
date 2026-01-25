//! 错误类型定义和转换

use pyo3::prelude::*;
use pyo3::exceptions::{PyValueError, PyRuntimeError};

/// 加密相关错误
pub struct CryptoError(pub grammers_crypto::Error);

impl From<CryptoError> for PyErr {
  fn from(err: CryptoError) -> PyErr {
    match err.0 {
      grammers_crypto::Error::InvalidBuffer => {
        PyValueError::new_err("Invalid ciphertext buffer length")
      }
      grammers_crypto::Error::AuthKeyMismatch => {
        PyValueError::new_err("Server auth_key mismatches with ours")
      }
      grammers_crypto::Error::MessageKeyMismatch => {
        PyValueError::new_err("Server msg_key mismatches with ours")
      }
    }
  }
}

impl From<grammers_crypto::Error> for CryptoError {
  fn from(err: grammers_crypto::Error) -> Self {
    CryptoError(err)
  }
}

/// 便捷的结果类型转换 trait
pub trait IntoPyResult<T> {
  fn into_py_result(self) -> PyResult<T>;
}

impl<T> IntoPyResult<T> for Result<T, grammers_crypto::Error> {
  fn into_py_result(self) -> PyResult<T> {
    self.map_err(|e| CryptoError(e).into())
  }
}