//! grammers-crypto 的 Python 绑定
//!
//! 提供 MTProto 加密相关功能

// mod errors;

// use pyo3::exceptions::PyValueError;
// use pyo3::types::PyBytes;

/*
mod aes;
mod hex;
mod rsa;
mod two_factor_auth;
*/

mod auth_key;
// mod deque_buffer;
// mod factorize;
// mod obfuscated;
mod sha;

#[pyo3::pymodule(name = "crypto")]
pub mod crypto_ {
    #[pymodule_export]
    #[allow(non_upper_case_globals)]
    const __doc__: &str = &"Cryptographic functions for MTProto protocol";

    #[pymodule_export]
    #[allow(non_upper_case_globals)]
    const __package__: &str = &"grammers";

    #[pymodule_export]
    use super::auth_key::PyAuthKey;

    // #[pymodule_export]
    // use super::deque_buffer::PyDequeBuffer;
}

//use factorize::factorize;
// use obfuscated::PyObfuscatedCipher;

// use errors::IntoPyResult;

// use grammers_crypto;

/*
/// 使用 MTProto 2.0 加密数据
///
/// 实现 Telegram 的 MTProto 2.0 加密算法，包括：
/// - 添加随机填充（12-1024 字节）
/// - 计算 msg_key
/// - AES-IGE 加密
/// - 添加 key_id 和 msg_key 前缀
///
/// Args:
///     plaintext: 要加密的明文数据
///     auth_key: 认证密钥
///
/// Returns:
///     加密后的完整消息 (key_id + msg_key + ciphertext)
#[pyfunction]
fn encrypt_data_v2<'py>(
  py: Python<'py>,
  plaintext: &[u8],
  auth_key: &PyAuthKey,
) -> Bound<'py, PyBytes> {
  let mut buffer = DequeBuffer::new();
  buffer.extend(plaintext.iter().copied());
  grammers_crypto::encrypt_data_v2(&mut buffer, &auth_key.inner);
  PyBytes::new(py, &buffer[..])
}

/// 使用 MTProto 2.0 解密数据
///
/// 实现 Telegram 的 MTProto 2.0 解密算法，包括：
/// - 验证 key_id
/// - 提取 msg_key
/// - AES-IGE 解密
/// - 验证 msg_key 正确性
///
/// Args:
///     ciphertext: 加密的消息 (key_id + msg_key + ciphertext)
///     auth_key: 认证密钥
///
/// Returns:
///     解密后的明文数据
///
/// Raises:
///     ValueError: 缓冲区无效、key_id 不匹配或 msg_key 验证失败
#[pyfunction]
fn decrypt_data_v2<'py>(
  py: Python<'py>,
  ciphertext: &[u8],
  auth_key: &PyAuthKey,
) -> PyResult<Bound<'py, PyBytes>> {
  let mut buffer = ciphertext.to_vec();
  let plaintext = grammers_crypto::decrypt_data_v2(&mut buffer, &auth_key.inner)
    .into_py_result()?;
  Ok(PyBytes::new(py, plaintext))
}

/// 从 nonce 生成 AES 密钥和 IV
///
/// 在 DH 密钥交换后使用，根据 server_nonce 和 new_nonce
/// 派生出用于后续通信的 AES 密钥和 IV。
///
/// Args:
///     server_nonce: 服务器 nonce (16 字节)
///     new_nonce: 客户端新 nonce (32 字节)
///
/// Returns:
///     (key, iv) 元组，各 32 字节
///
/// Raises:
///     ValueError: 如果参数长度不正确
#[pyfunction]
fn generate_key_data_from_nonce<'py>(
  py: Python<'py>,
  server_nonce: &[u8],
  new_nonce: &[u8],
) -> PyResult<(Bound<'py, PyBytes>, Bound<'py, PyBytes>)> {
  let server_nonce: &[u8; 16] = server_nonce.try_into().map_err(|_| {
    PyValueError::new_err(
      format!("server_nonce must be 16 bytes, got {}", server_nonce.len())
    )
  })?;

  let new_nonce: &[u8; 32] = new_nonce.try_into().map_err(|_| {
    PyValueError::new_err(
      format!("new_nonce must be 32 bytes, got {}", new_nonce.len())
    )
  })?;

  let (key, iv) = grammers_crypto::generate_key_data_from_nonce(server_nonce, new_nonce);

  Ok((PyBytes::new(py, &key), PyBytes::new(py, &iv)))
}


// ============================================================================
// AES-IGE 加密
// ============================================================================

/// AES-IGE 模式加密
///
/// Telegram 使用的特殊 AES 模式 (Infinite Garble Extension)。
/// 每个块的加密依赖于前一个明文块和前一个密文块。
///
/// Args:
///     data: 明文数据，长度必须是 16 的倍数
///     key: AES 密钥 (32 字节，AES-256)
///     iv: 初始化向量 (32 字节)
///
/// Returns:
///     加密后的数据
///
/// Raises:
///     ValueError: 参数长度不正确
#[pyfunction]
fn aes_ige_encrypt<'py>(
  py: Python<'py>,
  data: &[u8],
  key: &[u8],
  iv: &[u8],
) -> PyResult<Bound<'py, PyBytes>> {
  if data.len() % 16 != 0 {
    return Err(PyValueError::new_err(
      format!("Data length must be a multiple of 16 bytes, got {}", data.len())
    ));
  }

  let key: &[u8; 32] = key.try_into().map_err(|_| {
    PyValueError::new_err(format!("Key must be 32 bytes, got {}", key.len()))
  })?;

  let iv: &[u8; 32] = iv.try_into().map_err(|_| {
    PyValueError::new_err(format!("IV must be 32 bytes, got {}", iv.len()))
  })?;

  let mut buffer = data.to_vec();
  grammers_crypto::aes::ige_encrypt(&mut buffer, key, iv);
  Ok(PyBytes::new(py, &buffer))
}

/// AES-IGE 模式解密
///
/// Args:
///     data: 密文数据，长度必须是 16 的倍数
///     key: AES 密钥 (32 字节，AES-256)
///     iv: 初始化向量 (32 字节)
///
/// Returns:
///     解密后的数据
///
/// Raises:
///     ValueError: 参数长度不正确
#[pyfunction]
fn aes_ige_decrypt<'py>(
  py: Python<'py>,
  data: &[u8],
  key: &[u8],
  iv: &[u8],
) -> PyResult<Bound<'py, PyBytes>> {
  if data.len() % 16 != 0 {
    return Err(PyValueError::new_err(
      format!("Data length must be a multiple of 16 bytes, got {}", data.len())
    ));
  }

  let key: &[u8; 32] = key.try_into().map_err(|_| {
    PyValueError::new_err(format!("Key must be 32 bytes, got {}", key.len()))
  })?;

  let iv: &[u8; 32] = iv.try_into().map_err(|_| {
    PyValueError::new_err(format!("IV must be 32 bytes, got {}", iv.len()))
  })?;

  let mut buffer = data.to_vec();
  grammers_crypto::aes::ige_decrypt(&mut buffer, key, iv);
  Ok(PyBytes::new(py, &buffer))
}

// ============================================================================
// Hex 编解码
// ============================================================================

/// 将字节编码为十六进制字符串
///
/// Args:
///     data: 要编码的字节数据
///
/// Returns:
///     小写十六进制字符串
#[pyfunction]
fn hex_encode(data: &[u8]) -> String {
  grammers_crypto::hex::encode(data)
}

/// 将十六进制字符串解码为字节
///
/// Args:
///     hex_str: 十六进制字符串（大小写均可）
///
/// Returns:
///     解码后的字节数据
///
/// Raises:
///     ValueError: 无效的十六进制字符串
#[pyfunction]
fn hex_decode<'py>(py: Python<'py>, hex_str: &str) -> PyResult<Bound<'py, PyBytes>> {
  let data = grammers_crypto::hex::decode(hex_str).map_err(|e| {
    PyValueError::new_err(format!("Invalid hex string: {}", e))
  })?;
  Ok(PyBytes::new(py, &data))
}

// ============================================================================
// RSA 加密
// ============================================================================

/// RSA 加密（使用 Telegram 服务器公钥）
///
/// 使用指定指纹的 Telegram RSA 公钥加密数据。
/// 数据会先进行 SHA1 哈希再加密。
///
/// Args:
///     data: 要加密的数据
///     fingerprint: RSA 密钥指纹
///
/// Returns:
///     加密后的数据，如果找不到对应指纹的公钥则返回 None
#[pyfunction]
fn rsa_encrypt<'py>(
  py: Python<'py>,
  data: &[u8],
  fingerprint: i64,
) -> Option<Bound<'py, PyBytes>> {
  grammers_crypto::rsa::encrypt_hashed(data, fingerprint)
    .map(|encrypted| PyBytes::new(py, &encrypted))
}

// ============================================================================
// 两因素认证
// ============================================================================

/// 计算 2FA (SRP) 密码验证值
///
/// 实现 Telegram 的 SRP (Secure Remote Password) 协议，
/// 用于两因素认证密码验证。
///
/// Args:
///     password: 用户密码
///     salt1: 第一个盐值
///     salt2: 第二个盐值
///     g: SRP 生成器
///     p: SRP 大质数
///     g_b: 服务器的 g^b 值
///     a: 客户端随机数
///
/// Returns:
///     (M1, g_a) 元组，M1 是验证值，g_a 是客户端公钥
///
/// Raises:
///     RuntimeError: 计算失败
#[pyfunction]
fn calculate_2fa<'py>(
  py: Python<'py>,
  password: &[u8],
  salt1: &[u8],
  salt2: &[u8],
  g: i32,
  p: &[u8],
  g_b: &[u8],
  a: &[u8],
) -> PyResult<(Bound<'py, PyBytes>, Bound<'py, PyBytes>)> {
  let (m1, g_a) = grammers_crypto::two_factor_auth::calculate_2fa(
    password, salt1, salt2, g, p, g_b, a
  ).map_err(|e| {
    pyo3::exceptions::PyRuntimeError::new_err(
      format!("2FA calculation failed: {:?}", e)
    )
  })?;

  Ok((PyBytes::new(py, &m1), PyBytes::new(py, &g_a)))
}
*/
