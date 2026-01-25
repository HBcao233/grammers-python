/// 大整数因式分解
///
/// 使用 Pollard's rho 算法分解 pq 为两个质因数。
/// 这在 DH 密钥交换过程中用于验证服务器发送的 pq 值。
///
/// Args:
///     pq: 要分解的整数 (两个质数的乘积)
///
/// Returns:
///     (p, q) 元组，其中 p <= q
///
/// Example:
///     >>> p, q = factorize(15)
///     >>> print(f"{p} * {q} = 15")  # 3 * 5 = 15
#[pyo3::pyfunction]
fn factorize(pq: u64) -> (u64, u64) {
  grammers_crypto::factorize(pq)
}