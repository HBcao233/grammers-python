use std::io::{self, Write};

use grammers_tl_parser::tl::{Definition, Type};

use crate::Metadata;
use crate::grouper;
use crate::ignore_type;
use crate::rustifier;

fn write_enum<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    writeln!(
        file,
        "{indent}/// [Read `{name}` docs](https://core.telegram.org/type/{name}).",
        name = rustifier::TypeNameFmt(ty),
    )?;

    let type_name = rustifier::types::type_name(ty);
    writeln!(file, "{indent}#[derive(Debug, Clone)]")?;
    writeln!(file, "{indent}pub enum Py{} {{", type_name,)?;
    for d in metadata.defs_with_type(ty) {
        writeln!(
            file,
            "{indent}    {}({}),",
            rustifier::definitions::variant_name(d),
            rustifier::definitions::wrap_qual_name(d),
        )?;
    }
    writeln!(file, "{indent}}}")?;

    Ok(())
}

fn write_from<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    let type_name = rustifier::types::type_name(ty);
    writeln!(
        file,
        r#"{indent}impl pyo3::FromPyObject<'_, '_> for Py{} {{
{indent}    type Error = pyo3::PyErr;
{indent}    fn extract(obj: pyo3::Borrowed<'_, '_, pyo3::PyAny>) -> Result<Self, pyo3::PyErr> {{
{indent}        use pyo3::types::{{PyAnyMethods, PyTypeMethods}};"#,
        type_name,
    )?;
    for d in metadata.defs_with_type(ty) {
        writeln!(
            file,
            r#"{indent}        if let Ok(v) = obj.cast::<{}>() {{
{indent}          return Ok(Self::{}(v.to_owned().unbind().into()));
{indent}      }}"#,
            rustifier::definitions::qual_name(d),
            rustifier::definitions::variant_name(d),
        )?;
    }
    writeln!(
        file,
        r#"{indent}        Err(pyo3::PyErr::new::<pyo3::exceptions::PyTypeError, _>(
{indent}            format!("expected {}, got {{}}", obj.get_type().qualname()?)
{indent}        ))
{indent}    }}
{indent}}}"#,
        type_name,
    )?;
    Ok(())
}

fn write_into<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    let type_name = rustifier::types::type_name(ty);
    writeln!(
        file,
        r#"{indent}impl<'py> pyo3::IntoPyObject<'py> for Py{} {{
{indent}    type Target = pyo3::PyAny;
{indent}    type Output = pyo3::Bound<'py, pyo3::PyAny>;
{indent}    type Error = pyo3::PyErr;
{indent}    fn into_pyobject(self, py: pyo3::Python<'py>) -> Result<pyo3::Bound<'py, pyo3::PyAny>, pyo3::PyErr> {{
{indent}        Ok(match self {{"#,
        type_name,
    )?;
    for d in metadata.defs_with_type(ty) {
        writeln!(
            file,
            "{indent}            Self::{}(x) => x.0.into_bound(py).into_any(),",
            rustifier::definitions::variant_name(d),
        )?;
    }
    writeln!(
        file,
        r#"{indent}        }})
{indent}    }}
{indent}}}"#
    )?;
    Ok(())
}

fn write_serialize<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    let type_name = rustifier::types::type_name(ty);
    writeln!(
        file,
        "{indent}impl grammers_tl_types::Serializable for Py{} {{",
        type_name,
    )?;
    writeln!(
        file,
        "{indent}    fn serialize(&self, buf: &mut impl Extend<u8>) {{"
    )?;
    writeln!(file, "{indent}        use grammers_tl_types::Identifiable;")?;
    writeln!(file, "{indent}        match self {{")?;
    for d in metadata.defs_with_type(ty) {
        writeln!(
            file,
            "{indent}            Self::{}({}x) => {{",
            rustifier::definitions::variant_name(d),
            if d.params.is_empty() { "_" } else { "" },
        )?;
        writeln!(
            file,
            "{indent}                {}::CONSTRUCTOR_ID.serialize(buf);",
            rustifier::definitions::qual_name(d),
        )?;
        if !d.params.is_empty() {
            writeln!(file, "{indent}                x.serialize(buf);")?;
        }
        writeln!(file, "{indent}            }}")?;
    }
    writeln!(file, "{indent}        }}")?;
    writeln!(file, "{indent}    }}")?;
    writeln!(file, "{indent}}}")?;

    Ok(())
}

fn write_deserialize<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    let type_name = rustifier::types::type_name(ty);
    writeln!(
        file,
        "{indent}impl grammers_tl_types::Deserializable for Py{} {{",
        type_name,
    )?;
    writeln!(
        file,
        "{indent}    fn deserialize(buf: crate::Buffer) -> grammers_tl_types::deserialize::Result<Self> {{"
    )?;
    writeln!(file, "{indent}        use grammers_tl_types::Identifiable;")?;
    writeln!(file, "{indent}        let id = u32::deserialize(buf)?;")?;
    writeln!(file, "{indent}        Ok(match id {{")?;
    for d in metadata.defs_with_type(ty) {
        writeln!(
            file,
            "{indent}            {}::CONSTRUCTOR_ID => Self::{}({}),",
            rustifier::definitions::qual_name(d),
            rustifier::definitions::variant_name(d),
            format!(
                r#"{}::deserialize(buf)?.into()"#,
                rustifier::definitions::qual_name(d),
            ),
        )?;
    }
    writeln!(
        file,
        "{indent}            _ => return Err(grammers_tl_types::deserialize::Error::UnexpectedConstructor {{ id }}),"
    )?;
    writeln!(file, "{indent}        }})")?;
    writeln!(file, "{indent}    }}")?;
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
    writeln!(
      file,
      "{indent}    fn from({}x: {}) -> Self {{",
      if d.params.is_empty() {
        "_"
      } else {
        ""
      },
      qual_name,
    )?;
    writeln!(
      file,
      "{indent}        Self::{}({})",
      rustifier::definitions::variant_name(d),
      if d.params.is_empty() {
        format!("{} {{}}.into()", rustifier::definitions::qual_name(d))
      } else {
        "x.into()".to_string()
      },
    )?;
    writeln!(file, "{indent}    }}")?;
    writeln!(file, "{indent}}}")?;
  }
  Ok(())
}

fn write_from_tl<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    let tl_qual_name = rustifier::enums::tl_qual_name(ty);
    writeln!(
        file,
        r#"{indent}impl From<{tl_qual_name}> for Py{name} {{
{indent}    fn from(x: {tl_qual_name}) -> Self {{
{indent}        use {tl_qual_name} as E;
{indent}        match x {{"#,
        name = rustifier::types::type_name(ty),
    )?;
    for d in metadata.defs_with_type(ty) {
        let variant_name = rustifier::definitions::variant_name(d);
        writeln!(
            file, 
            r#"{indent}            E::{variant_name}{} => Self::{variant_name}({}),"#,
            if d.params.is_empty() {
                ""
            } else {
                "(x)"
            },
            if d.params.is_empty() {
                format!("{} {{}}.into()", rustifier::definitions::qual_name(d))
            } else {
                format!("{}.into()", if metadata.is_recursive_def(d) {
                    "(*x)"
                } else {
                    "x"
                })
            },
        )?;
    }
    writeln!(
        file, 
        r#"{indent}        }}
{indent}    }}
{indent}}}"#,
    )?;
    
    writeln!(
        file,
        r#"{indent}impl From<{tl_qual_name}> for crate::PyTLObject {{
{indent}    fn from(x: {tl_qual_name}) -> Self {{
{indent}        use {tl_qual_name} as E;
{indent}        match x {{"#,
    )?;
    for d in metadata.defs_with_type(ty) {
        let variant_name = rustifier::definitions::variant_name(d);
        let ns_type_name = rustifier::definitions::ns_type_name(d);
        writeln!(
            file, 
            r#"{indent}            E::{variant_name}{} => Self::{ns_type_name}({}),"#,
            if d.params.is_empty() {
                ""
            } else {
                "(x)"
            },
            if d.params.is_empty() {
                format!("{} {{}}.into()", rustifier::definitions::qual_name(d))
            } else {
                format!("{}.into()", if metadata.is_recursive_def(d) {
                    "(*x)"
                } else {
                    "x"
                })
            },
        )?;
    }
    writeln!(
        file, 
        r#"{indent}        }}
{indent}    }}
{indent}}}"#,
    )?;
    
    Ok(())
}

fn write_definition<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    write_enum(file, indent, ty, metadata)?;
    write_from(file, indent, ty, metadata)?;
    write_into(file, indent, ty, metadata)?;
    write_serialize(file, indent, ty, metadata)?;
    write_deserialize(file, indent, ty, metadata)?;
    write_impl_from(file, indent, ty, metadata)?;
    write_from_tl(file, indent, ty, metadata)?;
    writeln!(file)?;
    Ok(())
}

pub fn write_enums_mod<'a, W: Write>(
    mut file: &'a mut W,
    definitions: &[Definition],
    metadata: &Metadata,
) -> io::Result<()> {
    writeln!(file, "pub mod enums {{")?;

    let grouped = grouper::group_types_by_ns(definitions);
    let mut sorted_keys: Vec<&Option<String>> = grouped.keys().collect();
    sorted_keys.sort();

    for key in sorted_keys.into_iter() {
        // Begin possibly inner mod
        let indent = if let Some(ns) = key {
            writeln!(file, "    pub mod {ns} {{")?;
            "        "
        } else {
            "    "
        };

        for ty in grouped[key].iter().filter(|ty| !ignore_type(ty)) {
            write_definition(&mut file, indent, ty, metadata)?;
        }

        // End possibly inner mod
        if key.is_some() {
            writeln!(file, "    }}\n")?;
        }
    }

    writeln!(file, "}}")?;
    Ok(())
}
