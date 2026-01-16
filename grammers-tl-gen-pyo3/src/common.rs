use std::io::{self, Write};

use grammers_tl_parser::tl::{Definition, Category};

use crate::rustifier;
use crate::ignore_type;

fn write_enum_pytlrequest<W: Write>(
  file: &mut W,
  definitions: &[Definition],
) -> io::Result<()> {
  writeln!(file, "#[allow(non_camel_case_types)]")?;
  writeln!(file, "#[derive(Debug, FromPyObject)]")?;
  writeln!(file, "pub enum PyTLRequest {{")?;
  for def in definitions {
    if def.category == Category::Functions {
      writeln!(
        file,
        "    {}(pyo3::Py<{}>),",
        rustifier::definitions::ns_type_name(def),
        rustifier::functions::qual_name(def),
      )?;
    }
  }
  writeln!(file, "}}")?;
  Ok(())
}

fn write_serialize<W: Write>(
  file: &mut W,
  definitions: &[Definition],
) -> io::Result<()> {
  writeln!(file, "impl grammers_tl_types::Serializable for PyTLRequest {{")?;
  writeln!(file, "    fn serialize(&self, buf: &mut impl Extend<u8>) {{")?;
  writeln!(file, "        match self {{")?;
  for def in definitions {
    if def.category == Category::Functions {
      // let qual_name = rustifier::functions::qual_name(def);
      writeln!(
        file,
        "            Self::{}(x) => Python::attach(|py| {{",
        rustifier::definitions::ns_type_name(def),
      )?;
      writeln!(file, "                x.borrow(py).serialize(buf)")?;
      writeln!(file, "            }}),")?;
    }
  }
  writeln!(file, "        }}")?;
  writeln!(file, "    }}")?;
  writeln!(file, "}}")?;
  writeln!(file, r#"impl grammers_tl_types::RemoteCall for PyTLRequest {{
    type Return = crate::PyTLObject;
}}"#)?;
  Ok(())
}

fn write_enum_pytlobject<W: Write>(
  file: &mut W,
  definitions: &[Definition],
) -> io::Result<()> {
  writeln!(file, "#[allow(non_camel_case_types)]")?;
  writeln!(file, "#[derive(Debug, IntoPyObject)]")?;
  writeln!(file, "pub enum PyTLObject {{")?;
  for def in definitions {
    if def.category == Category::Types && !ignore_type(&def.ty) {
      writeln!(
        file,
        "    {}({}),",
        rustifier::definitions::ns_type_name(def),
        rustifier::definitions::qual_name(def),
      )?;
    }
  }
  writeln!(file, "}}")?;
  Ok(())
}

fn write_deserialize<W: Write>(
  file: &mut W,
  definitions: &[Definition],
) -> io::Result<()> {
  writeln!(file, "impl grammers_tl_types::Deserializable for PyTLObject {{")?;
  writeln!(file, "    fn deserialize(buf: crate::Buffer) -> grammers_tl_types::deserialize::Result<Self> {{")?;
  writeln!(file, "        use grammers_tl_types::Identifiable;")?;
  writeln!(file, "        let id = u32::deserialize(buf)?;")?;
  writeln!(file, "        Python::attach(|py| {{")?;
  writeln!(file, "            let base = PyClassInitializer::from(crate::TLObject {{}});")?;
  writeln!(file, "            match id {{")?;
  for def in definitions {
    if def.category == Category::Types && !ignore_type(&def.ty) {
      let qual_name = rustifier::definitions::ori_qual_name(def);
      let ns_type_name = rustifier::definitions::ns_type_name(def);
      writeln!(file, "            {}::CONSTRUCTOR_ID => {{", qual_name)?;
      writeln!(file, "                let x = {}::deserialize(buf)?;", qual_name)?;
      writeln!(file, "                let init = base.add_subclass(x);")?;
      writeln!(file, "                let res = pyo3::Py::new(py, init).expect(\"init\");")?;
      writeln!(file, "                Ok(Self::{}(res))", ns_type_name)?;
      writeln!(file, "            }},")?;
    }
  }
  writeln!(file, "                _ => Err(grammers_tl_types::deserialize::Error::UnexpectedConstructor {{ id }}),")?;
  writeln!(file, "            }}")?;
  writeln!(file, "        }})")?;
  writeln!(file, "    }}")?;
  writeln!(file, "}}")?;
  Ok(())
}

/// Write the entire module dedicated to enums.
pub fn write_enums_mod<'a, W: Write>(
  file: &'a mut W,
  definitions: &[Definition],
) -> io::Result<()> {
  writeln!(file, "use pyo3::{{Python, PyClassInitializer}};")?;
  writeln!(file, "use pyo3::{{FromPyObject, IntoPyObject}};")?;
  writeln!(file)?;
  write_enum_pytlrequest(file, definitions)?;
  write_serialize(file, definitions)?;
  writeln!(file)?;
  write_enum_pytlobject(file, definitions)?;
  write_deserialize(file, definitions)?;
  Ok(())
}
