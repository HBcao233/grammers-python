use std::env;
use std::fs::File;
use std::io::{self, BufRead, BufReader, BufWriter, Read};
use std::path::PathBuf;

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

/// Find the `// LAYER #` comment, and return its value if it's valid.
fn find_layer(file: &str) -> io::Result<Option<i32>> {
    const LAYER_MARK: &str = "LAYER";

    Ok(BufReader::new(File::open(file)?).lines().find_map(|line| {
        let line = line.unwrap();
        if line.trim().starts_with("//") {
            if let Some(pos) = line.find(LAYER_MARK) {
                if let Ok(layer) = line[pos + LAYER_MARK.len()..].trim().parse() {
                    return Some(layer);
                }
            }
        }

        None
    }))
}

fn main() -> io::Result<()> {
    println!("cargo:rerun-if-changed=tl/");
    println!("cargo:rerun-if-changed=build.rs");

    let layer = match find_layer("tl/api.tl")? {
        Some(x) => x,
        None => panic!("no layer information found in api.tl"),
    };

    let definitions = {
        let mut definitions = Vec::new();
        definitions.extend(load_tl("tl/api.tl")?);
        definitions.extend(load_tl("tl/mtproto.tl")?);
        definitions
    };

    let output_dir = PathBuf::from(&env::var("OUT_DIR").unwrap());

    let mut outputs = Outputs {
        common: BufWriter::new(File::create(output_dir.join("generated_common.rs"))?),
        types: BufWriter::new(File::create(output_dir.join("generated_types.rs"))?),
        types_: BufWriter::new(File::create(output_dir.join("generated_types_.rs"))?),
        functions: BufWriter::new(File::create(output_dir.join("generated_functions.rs"))?),
        functions_: BufWriter::new(File::create(output_dir.join("generated_functions_.rs"))?),
        enums: BufWriter::new(File::create(output_dir.join("generated_enums.rs"))?),
    };

    generate_rust_code(&mut outputs, &definitions, layer)?;

    outputs.flush()?;

    Ok(())
}
