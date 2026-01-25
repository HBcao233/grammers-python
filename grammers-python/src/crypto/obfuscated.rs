use pyo3::prelude::*;
use pyo3::types::PyBytes;
use grammers_crypto::ObfuscatedCipher;


/// MTProto 传输层混淆加密器
///
/// 用于混淆 TCP 连接数据，使流量不易被识别为 Telegram 通信。
/// 使用 AES-CTR 模式进行流加密。
///
/// Example:
///     >>> cipher = ObfuscatedCipher(enc_key, enc_iv, dec_key, dec_iv)
///     >>> encrypted = cipher.encrypt(b"data")
///     >>> decrypted = cipher.decrypt(encrypted)
#[pyclass(name = "ObfuscatedCipher", module = "grammers_python.crypto")]
pub struct PyObfuscatedCipher {
  inner: ObfuscatedCipher,
}

#[pymethods]
impl PyObfuscatedCipher {
  /// 创建混淆加密器
  ///
  /// Args:
  ///     encrypt_key: 加密密钥 (32 字节)
  ///     encrypt_iv: 加密 IV (16 字节)
  ///     decrypt_key: 解密密钥 (32 字节)
  ///     decrypt_iv: 解密 IV (16 字节)
  ///
  /// Raises:
  ///     ValueError: 如果参数长度不正确
  #[new]
  fn new(
    encrypt_key: &[u8],
    encrypt_iv: &[u8],
    decrypt_key: &[u8],
    decrypt_iv: &[u8],
  ) -> PyResult<Self> {
    let encrypt_key: [u8; 32] = encrypt_key.try_into().map_err(|_| {
      PyValueError::new_err(
        format!("encrypt_key must be 32 bytes, got {}", encrypt_key.len())
      )
    })?;

    let encrypt_iv: [u8; 16] = encrypt_iv.try_into().map_err(|_| {
      PyValueError::new_err(
        format!("encrypt_iv must be 16 bytes, got {}", encrypt_iv.len())
      )
    })?;

    let decrypt_key: [u8; 32] = decrypt_key.try_into().map_err(|_| {
      PyValueError::new_err(
        format!("decrypt_key must be 32 bytes, got {}", decrypt_key.len())
      )
    })?;

    let decrypt_iv: [u8; 16] = decrypt_iv.try_into().map_err(|_| {
      PyValueError::new_err(
        format!("decrypt_iv must be 16 bytes, got {}", decrypt_iv.len())
      )
    })?;

    Ok(Self {
      inner: ObfuscatedCipher::new(
        encrypt_key,
        encrypt_iv,
        decrypt_key,
        decrypt_iv,
      ),
    })
  }

  /// 加密数据
  ///
  /// 注意：这会修改加密器内部状态，同一数据再次加密会得到不同结果
  fn encrypt<'py>(&mut self, py: Python<'py>, data: &[u8]) -> Bound<'py, PyBytes> {
    let mut buffer = data.to_vec();
    self.inner.encrypt(&mut buffer);
    PyBytes::new(py, &buffer)
  }

  /// 解密数据
  ///
  /// 注意：必须按照加密顺序解密，否则会得到错误结果
  fn decrypt<'py>(&mut self, py: Python<'py>, data: &[u8]) -> Bound<'py, PyBytes> {
    let mut buffer = data.to_vec();
    self.inner.decrypt(&mut buffer);
    PyBytes::new(py, &buffer)
  }

  fn __repr__(&self) -> String {
    "ObfuscatedCipher(...)".to_string()
  }
}