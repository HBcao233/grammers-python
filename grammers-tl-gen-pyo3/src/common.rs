use std::io::{self, Write};

use grammers_tl_parser::tl::{Category, Definition};

use crate::ignore_type;
use crate::rustifier;

fn write_enum_pytlrequest<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(file, "#[allow(non_camel_case_types)]")?;
    writeln!(file, "#[derive(Debug, Clone)]")?;
    writeln!(file, "pub enum PyTLRequest {{")?;
    for def in definitions {
        if def.category == Category::Functions {
            writeln!(
                file,
                "    {}({}),",
                rustifier::definitions::ns_type_name(def),
                rustifier::functions::wrap_qual_name(def),
            )?;
        }
    }
    writeln!(file, "}}")?;
    Ok(())
}

fn write_rpc<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        "impl crate::Serializable for PyTLRequest {{"
    )?;
    writeln!(
        file,
        "    fn serialize(&self, buf: &mut impl Extend<u8>) {{"
    )?;
    writeln!(file, "        match self {{")?;
    for def in definitions {
        if def.category == Category::Functions {
            // let qual_name = rustifier::functions::wrap_qual_name(def);
            writeln!(
                file,
                "            Self::{}(x) => x.serialize(buf),",
                rustifier::definitions::ns_type_name(def),
            )?;
        }
    }
    writeln!(file, "        }}")?;
    writeln!(file, "    }}")?;
    writeln!(file, "}}")?;
    Ok(())
}

fn write_from_pytlrequest<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl pyo3::FromPyObject<'_, '_> for PyTLRequest {{
    type Error = pyo3::PyErr;
    fn extract(obj: pyo3::Borrowed<'_, '_, pyo3::PyAny>) -> Result<Self, pyo3::PyErr> {{
        use pyo3::types::{{PyAnyMethods, PyTypeMethods}};"#
    )?;
    for def in definitions {
        if def.category == Category::Functions {
            writeln!(
                file,
                r#"        if let Ok(v) = obj.cast::<{}>() {{
            return Ok(Self::{}(v.to_owned().unbind().into()));
        }}"#,
                rustifier::functions::qual_name(def),
                rustifier::definitions::ns_type_name(def),
            )?;
        }
    }
    writeln!(
        file,
        r#"        Err(pyo3::PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            format!("expected TLRequest, got {{}}", obj.get_type().qualname()?)
        ))
    }}
}}"#
    )?;
    Ok(())
}

fn write_into_pytlrequest<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl<'py> pyo3::IntoPyObject<'py> for PyTLRequest {{
    type Target = pyo3::PyAny;
    type Output = pyo3::Bound<'py, pyo3::PyAny>;
    type Error = pyo3::PyErr;
    fn into_pyobject(self, py: pyo3::Python<'py>) -> Result<pyo3::Bound<'py, pyo3::PyAny>, pyo3::PyErr> {{
        Ok(match self {{"#
    )?;
    for def in definitions {
        if def.category == Category::Functions {
            writeln!(
                file,
                "            Self::{}(x) => x.0.into_bound(py).into_any(),",
                // rustifier::functions::qual_name(def),
                rustifier::definitions::ns_type_name(def),
            )?;
        }
    }
    writeln!(
        file,
        r#"        }})
    }}
}}"#
    )?;
    Ok(())
}

fn write_enum_pytlobject<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(file, "#[allow(non_camel_case_types)]")?;
    writeln!(file, "#[derive(Debug, Clone)]")?;
    writeln!(file, "pub enum PyTLObject {{")?;
    for def in definitions {
        if def.category == Category::Types && !ignore_type(&def.ty) {
            writeln!(
                file,
                "    {}({}),",
                rustifier::definitions::ns_type_name(def),
                rustifier::definitions::wrap_qual_name(def),
            )?;
        }
    }
    writeln!(file, "}}")?;
    Ok(())
}

fn write_from_pytlobject<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl pyo3::FromPyObject<'_, '_> for PyTLObject {{
    type Error = pyo3::PyErr;
    fn extract(obj: pyo3::Borrowed<'_, '_, pyo3::PyAny>) -> Result<Self, pyo3::PyErr> {{
        use pyo3::types::{{PyAnyMethods, PyTypeMethods}};"#
    )?;
    for def in definitions {
        if def.category == Category::Types && !ignore_type(&def.ty) {
            writeln!(
                file,
                r#"        if let Ok(v) = obj.cast::<{}>() {{
            return Ok(Self::{}(v.to_owned().unbind().into()));
        }}"#,
                rustifier::definitions::qual_name(def),
                rustifier::definitions::ns_type_name(def),
            )?;
        }
    }
    writeln!(
        file,
        r#"        Err(pyo3::PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            format!("expected TLObject, got {{}}", obj.get_type().qualname()?)
        ))
    }}
}}"#
    )?;
    Ok(())
}

fn write_into_pytlobject<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl<'py> pyo3::IntoPyObject<'py> for PyTLObject {{
    type Target = pyo3::PyAny;
    type Output = pyo3::Bound<'py, pyo3::PyAny>;
    type Error = pyo3::PyErr;
    fn into_pyobject(self, py: pyo3::Python<'py>) -> Result<pyo3::Bound<'py, pyo3::PyAny>, pyo3::PyErr> {{
        Ok(match self {{"#
    )?;
    for def in definitions {
        if def.category == Category::Types && !ignore_type(&def.ty) {
            writeln!(
                file,
                "            Self::{}(x) => x.0.into_bound(py).into_any(),",
                // rustifier::functions::qual_name(def),
                rustifier::definitions::ns_type_name(def),
            )?;
        }
    }
    writeln!(
        file,
        r#"        }})
    }}
}}"#
    )?;
    Ok(())
}

fn write_serialize<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        "impl crate::Serializable for PyTLObject {{"
    )?;
    writeln!(
        file,
        "    fn serialize(&self, buf: &mut impl Extend<u8>) {{"
    )?;
    writeln!(file, "        match self {{")?;
    for def in definitions {
        if def.category == Category::Types && !ignore_type(&def.ty) {
            writeln!(
                file,
                "            Self::{}(x) => x.serialize(buf),",
                rustifier::definitions::ns_type_name(def),
            )?;
        }
    }
    writeln!(file, "        }}")?;
    writeln!(file, "    }}")?;
    writeln!(file, "}}")?;
    Ok(())
}

fn write_deserialize<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        "impl crate::Deserializable for PyTLObject {{"
    )?;
    writeln!(
        file,
        "    fn deserialize(buf: crate::Buffer) -> crate::deserialize::Result<Self> {{"
    )?;
    writeln!(file, "        use crate::Identifiable;")?;
    writeln!(file, "        let id = u32::deserialize(buf)?;")?;
    writeln!(file, "        match id {{")?;
    for def in definitions {
        if def.category == Category::Types && !ignore_type(&def.ty) {
            let qual_name = rustifier::definitions::qual_name(def);
            // let ns_type_name = rustifier::definitions::ns_type_name(def);
            writeln!(
                file,
                "            {name}::CONSTRUCTOR_ID => Ok({name}::deserialize(buf)?.into()),",
                name = qual_name,
            )?;
        }
    }
    writeln!(
        file,
        "            _ => Err(crate::deserialize::Error::UnexpectedConstructor {{ id }}),"
    )?;
    writeln!(file, "        }}")?;
    writeln!(file, "    }}")?;
    writeln!(file, "}}")?;
    Ok(())
}

/// Write the entire module dedicated to enums.
pub fn write_mod<'a, W: Write>(
    file: &'a mut W,
    definitions: &[Definition],
    layer: i32,
) -> io::Result<()> {
    writeln!(
        file,
        r#"/// The schema layer from which the definitions were generated.
pub const LAYER: i32 = {layer};
"#
    )?;
    writeln!(
        file,
        r#"
/// Return the name from the `.tl` definition corresponding to the provided definition identifier.
pub fn name_for_id(id: u32) -> &'static str {{
    match id {{
        0x1cb5c415 => "vector","#
    )?;
    for def in definitions {
        writeln!(
            file,
            r#"        0x{:x} => "{}","#,
            def.id,
            def.full_name()
        )?;
    }
    writeln!(
        file,
        r#"
        _ => "(unknown)",
    }}
}}
        "#,
    )?;
    
    write_enum_pytlrequest(file, definitions)?;
    write_from_pytlrequest(file, definitions)?;
    write_into_pytlrequest(file, definitions)?;
    write_rpc(file, definitions)?;

    writeln!(file)?;

    write_enum_pytlobject(file, definitions)?;
    write_from_pytlobject(file, definitions)?;
    write_into_pytlobject(file, definitions)?;
    write_serialize(file, definitions)?;
    write_deserialize(file, definitions)?;

    Ok(())
}
