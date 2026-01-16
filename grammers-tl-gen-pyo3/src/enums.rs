use std::io::{self, Write};

use grammers_tl_parser::tl::{Definition, Type};

use crate::grouper;
use crate::rustifier;
use crate::Metadata;
use crate::ignore_type;

fn write_enum<W: Write>(
  file: &mut W,
  file_: &mut W, 
  indent: &str,
  ty: &Type,
  metadata: &Metadata,
) -> io::Result<()> {
  writeln!(
    file,
    "/// [Read `{name}` docs](https://core.telegram.org/type/{name}).",
    name = rustifier::TypeNameFmt(ty),
  )?;
  
  let type_name = rustifier::types::type_name(ty);
  writeln!(file_, "{indent}#[pymodule_export]")?;
  writeln!(
    file_, 
    "{indent}use crate::enums::{}Py{};",
    if ty.namespace.len() > 0 {
      format!("{}{}", ty.namespace[0], "::")
    } else { "".to_string() },
    type_name,
  )?;
  
  writeln!(file, "{indent}#[derive(Debug, Clone)]")?;
  writeln!(file, "{indent}#[pyo3::pyclass]")?;
  writeln!(
    file, 
    "{indent}pub enum Py{} {{",
    type_name,
  )?;
  for d in metadata.defs_with_type(ty) {
    writeln!(
      file,
      "{indent}    {}({}),",
      rustifier::definitions::variant_name(d),
      if d.params.is_empty() {
        "".to_string()
      } else {
        rustifier::definitions::qual_name(d)
      },
    )?;
  }
  writeln!(file, "{indent}}}")?;
  Ok(())
}

fn write_impl_from<W: Write>(
  file: &mut W,
  indent: &str,
  ty: &Type,
  metadata: &Metadata,
) -> io::Result<()> {
  for d in metadata.defs_with_type(ty) {
    let qual_name = rustifier::definitions::qual_name(d);
    writeln!(
      file, 
      "{indent}impl From<{}> for Py{} {{",
      qual_name,
      rustifier::types::type_name(ty),
    )?;
    writeln!(file, "{indent}    fn from(x: {}) -> Self {{", qual_name)?;
    writeln!(
      file, 
      "{indent}        Self::{}(x)", 
      rustifier::definitions::variant_name(d)
    )?;
    writeln!(file, "{indent}    }}")?;
    writeln!(file, "{indent}}}")?;
  }
  Ok(())
}

fn write_definition<W: Write>(
  file: &mut W,
  file_: &mut W, 
  indent: &str,
  ty: &Type,
  metadata: &Metadata,
) -> io::Result<()> {
  write_enum(file, file_, indent, ty, metadata)?;
  write_impl_from(file, indent, ty, metadata)?;
  Ok(())
}

pub fn write_enums_mod<'a, W: Write>(
  mut file: &'a mut W,
  mut file_: &'a mut W,
  definitions: &[Definition],
  metadata: &Metadata,
) -> io::Result<()> {
  writeln!(file, "pub mod enums {{")?;
  writeln!(file_, "#[pyo3::pymodule(name = \"enums\")]")?;
  writeln!(file_, "pub mod enums_ {{")?;
  
  let grouped = grouper::group_types_by_ns(definitions);
  let mut sorted_keys: Vec<&Option<String>> = grouped.keys().collect();
  sorted_keys.sort();
  
  for key in sorted_keys.into_iter() {
    // Begin possibly inner mod
    let indent = if let Some(ns) = key {
      writeln!(file, "    pub mod {ns} {{")?;
      writeln!(file_, "    #[pyo3::pymodule]")?;
      writeln!(file_, "    pub mod {ns} {{")?;
      "        "
    } else {
      "    "
    };

    for ty in grouped[key].iter().filter(|ty| !ignore_type(ty)) {
      write_definition(&mut file, &mut file_, indent, ty, metadata)?;
    }

    // End possibly inner mod
    if key.is_some() {
      writeln!(file, "    }}\n")?;
      writeln!(file_, "    }}\n")?;
    }
  }
  
  writeln!(file, "}}")?;
  writeln!(file_, "}}")?;
  Ok(())
}