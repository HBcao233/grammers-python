macro_rules! include_generated {
  ($($file:literal),* $(,)?) => {
    $(
      include!(concat!(
        // "out", 
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
  "functions.rs",
  "enums.rs",
  "types_.rs",
  "functions_.rs",
  "enums_.rs",
);
