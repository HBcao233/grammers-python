use std::env;
use std::fs::File;
use std::io::{self, BufWriter, Read};
use std::path::Path;

use grammers_tl_parser::parse_tl_file;
use grammers_tl_parser::tl::Definition;

use grammers_tl_gen_pyo3::{Outputs, generate_rust_code};


fn load_tl(file: &str) -> io::Result<Vec<Definition>> {
  let mut file = File::open(file)?;
  let mut contents = String::new();
  file.read_to_string(&mut contents)?;
  Ok(parse_tl_file(&contents)
    .filter_map(|d| match d {
      Ok(d) => Some(d),
      Err(e) => {
        eprintln!("TL: parse error: {e:?}");
        None
      }
    })
    .collect())
}

fn main() -> std::io::Result<()> {
  let definitions = {
    let mut definitions = Vec::new();
    definitions.extend(load_tl("tl/api.tl")?);
    definitions.extend(load_tl("tl/mtproto.tl")?);
    definitions
  };
  
  let output_dir = Path::new(&env::var("OUT_DIR").unwrap()).to_path_buf();
  let mut outputs = Outputs {
    common: BufWriter::new(File::create(output_dir.join("generated_common.rs"))?),
    types: BufWriter::new(File::create(output_dir.join("generated_types.rs"))?),
    types_: BufWriter::new(File::create(output_dir.join("generated_types_.rs"))?),
    functions: BufWriter::new(File::create(output_dir.join("generated_functions.rs"))?),
    functions_: BufWriter::new(File::create(output_dir.join("generated_functions_.rs"))?),
    enums: BufWriter::new(File::create(output_dir.join("generated_enums.rs"))?),
  };
  
  generate_rust_code(&mut outputs, &definitions)?;

  outputs.flush()?;
  
  Ok(())
}