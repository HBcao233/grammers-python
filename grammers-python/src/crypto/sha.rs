#[macro_export]
macro_rules! sha1 (
  ( $( $x:expr ),* ) => ({
    use sha1::{Digest, Sha1};
    let mut hasher = Sha1::new();
    $(
      hasher.update($x);
    )+
    let sha: [u8; 20] = hasher.finalize().into();
    sha
  })
);
