mod metadata;
mod grouper;
mod rustifier;
mod structs;
mod common;
mod enums;

use std::io::{self, Write};

use metadata::Metadata;

use grammers_tl_parser::tl::{Category, Definition, Type};

pub struct Outputs<W: Write> {
  /// Writer to the file containing all of the boxed [`Category::Functions`] constructors.
  pub common: W,
  /// Writer to the file containing all of the concrete [`Category::Types`] constructors.
  pub types: W,
  pub types_: W,
  /// Writer to the file containing all of the [`Category::Functions`] constructors.
  pub functions: W,
  pub functions_: W,
  /// Writer to the file containing all of the boxed [`Category::Types`] constructors.
  pub enums: W,
}
impl<W: Write> Outputs<W> {
  /// Flush all writers sequentially.
  pub fn flush(&mut self) -> std::io::Result<()> {
    self.common.flush()?;
    self.types.flush()?;
    self.types_.flush()?;
    self.functions.flush()?;
    self.functions_.flush()?;
    self.enums.flush()?;
    Ok(())
  }
}

/// Don't generate types for definitions of this type,
/// since they are "core" types and treated differently.
const SPECIAL_CASED_TYPES: [&str; 1] = ["Bool"];

fn ignore_type(ty: &Type) -> bool {
  SPECIAL_CASED_TYPES.iter().any(|&x| x == ty.name)
}

pub fn generate_rust_code<W: Write>(
  outputs: &mut Outputs<W>,
  definitions: &[Definition],
) -> io::Result<()> {
  common::write_enums_mod(&mut outputs.common, definitions)?;
  
  let metadata = Metadata::new(definitions);
  
  structs::write_category_mod(
    &mut outputs.types,
    &mut outputs.types_,
    Category::Types,
    definitions,
    &metadata,
  )?;
  
  structs::write_category_mod(
    &mut outputs.functions,
    &mut outputs.functions_,
    Category::Functions,
    definitions,
    &metadata,
  )?;
  
  enums::write_enums_mod(
    &mut outputs.enums,
    definitions,
    &metadata,
  )?;
  Ok(())
}