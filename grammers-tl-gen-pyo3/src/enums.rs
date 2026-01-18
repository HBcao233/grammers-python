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

fn write_stubtype<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    let type_name = rustifier::types::type_name(ty);
    let ns = if metadata.defs_with_type(ty).is_empty() {
        "".to_string()
    } else {
        let d = metadata.defs_with_type(ty)[0];
        if d.namespace.is_empty() {
            "".to_string()
        } else {
            ".".to_string() + &d.namespace[0]
        }
    };
    let type_hint = metadata
        .defs_with_type(ty)
        .iter()
        .map(|d| {
            let mut result = String::new();
            result.push_str("grammers.tl.types.");
            d.namespace.iter().for_each(|ns| {
                result.push_str(ns);
                result.push_str(".");
            });
            result.push_str(&rustifier::definitions::type_name(d));
            result
        })
        .collect::<Vec<String>>()
        .join(" | ");
    writeln!(
        file,
        r#"{indent}#[cfg(feature = "stub-gen")]
{indent}impl pyo3_stub_gen::PyStubType for Py{} {{
{indent}    fn type_output() -> pyo3_stub_gen::TypeInfo {{
{indent}        pyo3_stub_gen::TypeInfo {{
{indent}            name: "{}".to_string(),
{indent}            import: vec!["grammers.tl.types{}".into()].into_iter().collect(),
{indent}        }}
{indent}    }}
{indent}}}"#,
        type_name, type_hint, ns,
    )?;
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

/*
fn write_impl_from<W: Write>(
  file: &mut W,
  indent: &str,
  ty: &Type,
  metadata: &Metadata,
) -> io::Result<()> {
  for d in metadata.defs_with_type(ty) {
    let qual_name = rustifier::definitions::wrap_qual_name(d);
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
        ""
      } else {
        "x"
      },
    )?;
    writeln!(file, "{indent}    }}")?;
    writeln!(file, "{indent}}}")?;
  }
  Ok(())
}*/

fn write_definition<W: Write>(
    file: &mut W,
    indent: &str,
    ty: &Type,
    metadata: &Metadata,
) -> io::Result<()> {
    write_enum(file, indent, ty, metadata)?;
    write_stubtype(file, indent, ty, metadata)?;
    write_from(file, indent, ty, metadata)?;
    write_into(file, indent, ty, metadata)?;
    write_serialize(file, indent, ty, metadata)?;
    write_deserialize(file, indent, ty, metadata)?;
    // write_impl_from(file, indent, ty, metadata)?;
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
