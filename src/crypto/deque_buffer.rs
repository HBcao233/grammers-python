use pyo3::prelude::*;
use pyo3::types::PyBytes;
use grammers_crypto::DequeBuffer;

/// 高效的双端字节缓冲区
///
/// 支持在头部和尾部快速添加数据，专为 MTProto 消息构建优化。
/// 避免了频繁的内存移动操作。
///
/// Example:
///     >>> buf = DequeBuffer()
///     >>> buf.extend(b"world")
///     >>> buf.extend_front(b"hello ")
///     >>> print(buf.to_bytes())  # b"hello world"
use grammers_crypto::DequeBuffer;

#[cfg(feature = "stub-gen")]
use pyo3_stub_gen::derive::*;


/// A growable buffer with the properties of a deque.
///
/// Unlike the standard [`VecDeque`](std::collections::VecDeque),
/// this buffer is designed to not need explicit calls to `make_contiguous`
/// and minimize the amount of memory moves.
#[cfg_attr(feature = "stub-gen", gen_stub_pyclass)]
#[pyclass(name = "DequeBuffer", module = "grammers.crypto")]
pub struct PyDequeBuffer {
  inner: DequeBuffer<u8>,
}

#[cfg_attr(feature = "stub-gen", gen_stub_pymethods)]
#[pymethods]
impl PyDequeBuffer {
  /// 创建空的缓冲区
  #[new]
  fn new() -> Self {
    Self {
      inner: DequeBuffer::new(),
    }
  }

  /// 从字节数据创建缓冲区
  #[staticmethod]
  fn from_bytes(data: &[u8]) -> Self {
    let mut buffer = DequeBuffer::new();
    buffer.extend(data.iter().copied());
    Self { inner: buffer }
  }

  /// 在尾部追加数据
  fn extend(&mut self, data: &[u8]) {
    self.inner.extend(data.iter().copied());
  }

  /// 在头部追加数据
  fn extend_front(&mut self, data: &[u8]) {
    self.inner.extend_front(data);
  }

  /// 缓冲区当前长度
  fn __len__(&self) -> usize {
    self.inner.len()
  }

  /// 检查缓冲区是否为空
  fn is_empty(&self) -> bool {
    self.inner.is_empty()
  }

  /// 转换为 bytes 对象
  fn to_bytes<'py>(&self, py: Python<'py>) -> Bound<'py, PyBytes> {
    PyBytes::new(py, &self.inner[..])
  }

  /// 清空缓冲区
  fn clear(&mut self) {
    self.inner.clear();
  }

  fn __repr__(&self) -> String {
    format!("DequeBuffer(len={})", self.inner.len())
  }

  fn __bytes__<'py>(&self, py: Python<'py>) -> Bound<'py, PyBytes> {
    self.to_bytes(py)
  }
}