macro_rules! include_generated {
  ($($file:literal),* $(,)?) => {
    $(
      include!(concat!(
        env!("OUT_DIR"),
        "/generated_",
        $file,
      ));
    )*
  };
}

include_generated!(
    "common.rs",
    "types.rs",
    "types_.rs",
    "functions.rs",
    "functions_.rs",
    "enums.rs",
);
