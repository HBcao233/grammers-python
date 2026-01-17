use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::exceptions::PyValueError;
use grammers_crypto::AuthKey;
use crate::sha1;

#[cfg(feature = "stub-gen")]
use pyo3_stub_gen::derive::*;


#[derive(FromPyObject)]
enum BytesOrStr {
  #[pyo3(transparent)]
  Bytes(Vec<u8>),
  #[pyo3(transparent)]
  Str(String),
}

#[cfg(feature = "stub-gen")]
impl pyo3_stub_gen::PyStubType for BytesOrStr {
  fn type_output() -> pyo3_stub_gen::TypeInfo {
    pyo3_stub_gen::TypeInfo {
      name: "builtins.bytes | builtins.str".to_string(),
      import: vec!["builtins".into()].into_iter().collect(),
    }
  }
}


/// Telegram's [Authorization Key](https://core.telegram.org/mtproto/auth_key).
///
/// This library does not provide the means to generate a valid key,
/// because doing so relies on (de-)serializing Telegram types.
#[cfg_attr(feature = "stub-gen", gen_stub_pyclass)]
#[pyclass(name = "AuthKey", module = "grammers.crypto")]
#[derive(Clone)]
pub struct PyAuthKey {
  inner: AuthKey,
  id: [u8; 8],
}

#[cfg_attr(feature = "stub-gen", gen_stub_pymethods)]
#[pymethods]
impl PyAuthKey {
  /// 从 256 字节数据或创建 AuthKey
  ///
  /// Args:
  ///     data: 256 字节的密钥数据
  ///
  /// Raises:
  ///     ValueError: 如果数据长度不是 256 字节
  #[new]
  #[pyo3(signature = (data), text_signature = "(data: bytes | str)")]
  fn new(data: BytesOrStr) -> PyResult<Self> {
    match data {
      BytesOrStr::Str(s) => Self::from_hex(&s),
      BytesOrStr::Bytes(b) => {
        let data: [u8; 256] = (*b).try_into().map_err(|_| {
          PyValueError::new_err(
            format!("AuthKey data must be exactly 256 bytes, got {}", b.len())
          )
        })?;
      
        let sha = sha1!(&data);
        let id = {
          let mut buffer = [0; 8];
          buffer.copy_from_slice(&sha[12..12 + 8]);
          buffer
        };
    
        Ok(Self {
          inner: AuthKey::from_bytes(data),
          id,
        })
      },
    }
  }

  /// 完整的密钥数据 (256 字节)
  #[getter]
  fn data<'py>(&self, py: Python<'py>) -> Bound<'py, PyBytes> {
    PyBytes::new(py, &self.inner.to_bytes())
  }

  /// 从十六进制字符串创建 AuthKey
  ///
  /// Args:
  ///     hex_str: 512 字符的十六进制字符串
  ///
  /// Returns:
  ///     AuthKey 实例
  #[staticmethod]
  fn from_hex(hex_str: &str) -> PyResult<Self> {
    let data = grammers_crypto::hex::opt_from_hex(hex_str).ok_or_else(|| {
      PyValueError::new_err(format!("Invalid hex string: {}", hex_str))
    })?;
    Self::new(BytesOrStr::Bytes(data))
  }

  /// 转换为十六进制字符串
  fn to_hex(&self) -> String {
    grammers_crypto::hex::to_hex(&self.inner.to_bytes())
  }

  fn __repr__(&self) -> String {
    format!(
      "<AuthKey id={}>",
      format!("{:?}", grammers_crypto::hex::to_hex(&self.id))
    )
  }

  fn __eq__(&self, other: &Self) -> bool {
    self.inner == other.inner
  }

  fn __hash__(&self) -> u64 {
    use std::hash::{Hash, Hasher};
    use std::collections::hash_map::DefaultHasher;
    let mut hasher = DefaultHasher::new();
    self.id.hash(&mut hasher);
    hasher.finish()
  }
}
