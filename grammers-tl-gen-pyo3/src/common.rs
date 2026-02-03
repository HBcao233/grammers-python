use std::io::{self, Write};

use grammers_tl_parser::tl::{Category, Definition};

use crate::ignore_type;
use crate::rustifier;

fn write_enum_tlrequest<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(file, "#[allow(non_camel_case_types)]")?;
    writeln!(file, "#[derive(Debug, Clone)]")?;
    writeln!(file, "pub enum TLRequestLike {{")?;
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
        "impl grammers_tl_types::Serializable for TLRequestLike {{"
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

fn write_from_tlrequest<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl pyo3::FromPyObject<'_, '_> for TLRequestLike {{
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

fn write_into_tlrequest<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl<'py> pyo3::IntoPyObject<'py> for TLRequestLike {{
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

fn write_enum_tlobject<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(file, "#[allow(non_camel_case_types)]")?;
    writeln!(file, "#[derive(Debug, Clone)]")?;
    writeln!(file, "pub enum TLObjectLike {{
    Vec(Vec<TLObjectLike>),")?;
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

fn write_from_tlobject<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl pyo3::FromPyObject<'_, '_> for crate::TLObjectLike {{
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

fn write_into_tlobject<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    writeln!(
        file,
        r#"impl<'py> pyo3::IntoPyObject<'py> for TLObjectLike {{
    type Target = pyo3::PyAny;
    type Output = pyo3::Bound<'py, pyo3::PyAny>;
    type Error = pyo3::PyErr;
    fn into_pyobject(self, py: pyo3::Python<'py>) -> Result<pyo3::Bound<'py, pyo3::PyAny>, pyo3::PyErr> {{
        Ok(match self {{
            Self::Vec(x) => x.into_pyobject(py)?,"#
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
        r#"impl grammers_tl_types::Serializable for TLObjectLike {{
    fn serialize(&self, buf: &mut impl Extend<u8>) {{
        match self {{
            Self::Vec(x) => x.into_iter().for_each(|x| x.serialize(buf)),"#,
    )?;
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
        r#"impl grammers_tl_types::Deserializable for TLObjectLike {{
    fn deserialize(buf: crate::Buffer) -> grammers_tl_types::deserialize::Result<Self> {{
        use grammers_tl_types::Identifiable;
        let id = u32::deserialize(buf)?;
        Ok(match id {{
            0x1cb5c415u32 => {{
                let len = u32::deserialize(buf)?;
                TLObjectLike::Vec(
                    (0..len)
                    .map(|_| TLObjectLike::deserialize(buf))
                    .collect::<grammers_tl_types::deserialize::Result<Vec<TLObjectLike>>>()?
                )
            }},"#,
    )?;
    for def in definitions {
        if def.category == Category::Types && !ignore_type(&def.ty) {
            let qual_name = rustifier::definitions::qual_name(def);
            // let ns_type_name = rustifier::definitions::ns_type_name(def);
            writeln!(
                file,
                "            {name}::CONSTRUCTOR_ID => {name}::deserialize(buf)?.into(),",
                name = qual_name,
            )?;
        }
    }
    writeln!(
        file,
        r#"            _ => return Err(grammers_tl_types::deserialize::Error::UnexpectedConstructor {{ id }}),
        }})
    }}
}}"#
    )?;
    Ok(())
}

fn write_from_tl<W: Write>(file: &mut W, definitions: &[Definition]) -> io::Result<()> {
    for def in definitions {
        if def.category == Category::Types && !ignore_type(&def.ty) {
            let tl_qual_name = rustifier::definitions::tl_qual_name(def);
            writeln!(
                file,
                r#"impl From<{tl_qual_name}> for TLObjectLike {{
    fn from(x: {tl_qual_name}) -> Self {{
        Self::{}(x.into())
    }}
}}"#,
                rustifier::definitions::ns_type_name(def),
            )?;
        }
    }

    Ok(())
}

/// Write the entire module dedicated to enums.
pub fn write_mod<'a, W: Write>(
    file: &'a mut W,
    definitions: &[Definition],
    _layer: i32,
) -> io::Result<()> {
    write_enum_tlrequest(file, definitions)?;
    write_from_tlrequest(file, definitions)?;
    write_into_tlrequest(file, definitions)?;
    write_rpc(file, definitions)?;

    writeln!(file)?;

    write_enum_tlobject(file, definitions)?;
    write_from_tlobject(file, definitions)?;
    write_into_tlobject(file, definitions)?;
    write_serialize(file, definitions)?;
    write_deserialize(file, definitions)?;
    write_from_tl(file, definitions)?;

    Ok(())
}
