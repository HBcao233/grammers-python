use std::io::{self, Write};

use grammers_tl_parser::tl::{Category, Definition, ParameterType};

use crate::Metadata;
use crate::grouper;
use crate::ignore_type;
use crate::rustifier;

/// Defines the `struct` corresponding to the definition:
///
/// ```ignore
/// #[pyo3::pyclass(name = "Name", module = "grammers.tl[.ns]", extends = crate::TLObject)]
/// pub struct PyName {
///     pub field: Type,
/// }
/// ```
fn write_struct<W: Write>(
    file: &mut W,
    file_: &mut W,
    indent: &str,
    def: &Definition,
) -> io::Result<()> {
    // Define struct
    writeln!(
        file,
        "{indent}/// [Read `{name}` docs](https://core.telegram.org/{kind}/{name}).
{indent}///
{indent}/// Generated from the following TL definition:
{indent}/// ```tl
{indent}/// {def}
{indent}/// ```",
        name = def.full_name(),
        kind = match def.category {
            Category::Types => "constructor",
            Category::Functions => "method",
        },
        def = def,
    )?;

    let type_name = rustifier::definitions::type_name(def);
    writeln!(file_, "{indent}#[pymodule_export]")?;
    writeln!(
        file_,
        "{indent}use crate::{}::{}Py{};",
        match def.category {
            Category::Functions => "functions",
            Category::Types => "types",
        },
        if def.namespace.len() > 0 {
            format!("{}{}", def.namespace[0], "::")
        } else {
            "".to_string()
        },
        type_name,
    )?;

    writeln!(file, "{indent}#[derive(Debug, Clone)]")?;
    writeln!(
        file,
        "{}#[pyo3::pyclass(name = \"{}\", module = \"grammers.tl{}\", extends = crate::{})]",
        indent,
        type_name,
        if def.namespace.is_empty() {
            "".to_string()
        } else {
            format!(".{}", def.namespace[0])
        },
        match def.category {
            Category::Types => "TLObject",
            Category::Functions => "TLRequest",
        },
    )?;
    writeln!(file, "{}pub struct Py{} {{", indent, type_name,)?;

    for param in def.params.iter() {
        match &param.ty {
            ParameterType::Flags => {
                // Flags are computed on-the-fly, not stored
            }
            ParameterType::Normal { .. } => {
                writeln!(file, "{}    #[pyo3(get, set)]", indent,)?;
                writeln!(
                    file,
                    "{}    pub {}: {},",
                    indent,
                    rustifier::parameters::attr_name(param),
                    rustifier::parameters::qual_name(param),
                )?;
            }
        }
    }
    writeln!(file, "{indent}}}")?;

    writeln!(
        file,
        r#"{indent}#[repr(transparent)]
{indent}#[derive(Debug, pyo3::FromPyObject, pyo3::IntoPyObject)]
{indent}pub struct Py{name}Wrapper(pub pyo3::Py<Py{name}>);
{indent}impl Clone for Py{name}Wrapper {{
{indent}    fn clone(&self) -> Self {{
{indent}        pyo3::Python::attach(|py| self.0.borrow(py).clone()).into()
{indent}    }}
{indent}}}
{indent}impl From<pyo3::Py<Py{name}>> for Py{name}Wrapper {{
{indent}    fn from(x: pyo3::Py<Py{name}>) -> Self {{
{indent}        Self(x)
{indent}    }}
{indent}}}
{indent}impl From<Py{name}> for Py{name}Wrapper {{
{indent}    fn from(x: Py{name}) -> Self {{
{indent}        pyo3::Python::attach(|py| {{
{indent}            let init = pyo3::PyClassInitializer::from(crate::{base} {{}});
{indent}            pyo3::Py::new(py, init.add_subclass(x)).expect("init")
{indent}        }}).into()
{indent}    }}
{indent}}}
{indent}impl From<Py{name}> for crate::Py{base} {{
{indent}    fn from(x: Py{name}) -> Self {{
{indent}        Self::{ns_name}(x.into())
{indent}    }}
{indent}}}"#,
        name = type_name,
        base = match def.category {
            Category::Functions => "TLRequest",
            Category::Types => "TLObject",
        },
        ns_name = rustifier::definitions::ns_type_name(def),
    )?;

    Ok(())
}

/// Defines the `impl` corresponding to the definition:
///
/// ```ignore
/// #[pyo3::pymethods]
/// impl PyName {
///     #[classattr]
///     const CONSTRUCTOR_ID: u32 = 123;
///
///     #[new]
///     fn new(
///         param: param_type,
///     ) -> Self {
///         Self {
///             param: param_type,
///         }
///     }
/// 
///     fn to_bytes(&self) -> Vec<u8> {
///     }
/// 
///     fn to_dict(&self) -> pyo3::PyResult<pyo3::Py<pyo3::types::PyDict>> {
///     }
/// }
/// ```
fn write_impl<W: Write>(file: &mut W, indent: &str, def: &Definition) -> io::Result<()> {
    let type_name = rustifier::definitions::type_name(def);
    writeln!(file, "{indent}#[pyo3::pymethods]")?;
    writeln!(file, "{}impl Py{} {{", indent, type_name,)?;

    writeln!(file, "{indent}    #[classattr]")?;
    writeln!(
        file,
        "{indent}    const CONSTRUCTOR_ID: u32 = {};\n",
        def.id
    )?;
    writeln!(file, "{indent}    #[new]")?;
    write!(file, "{indent}    fn new(")?;
    if def.params.len() != 0 {
        writeln!(file)?;
    }
    for param in def.params.iter() {
        match &param.ty {
            ParameterType::Flags => {
                // Flags are computed on-the-fly, not stored
            }
            ParameterType::Normal { .. } => {
                writeln!(
                    file,
                    "{}        {}: {},",
                    indent,
                    rustifier::parameters::attr_name(param),
                    rustifier::parameters::qual_name(param),
                )?;
            }
        }
    }
    if def.params.len() != 0 {
        write!(file, "{indent}    ")?;
    }
    writeln!(
        file,
        ") -> (Py{}, crate::{}) {{",
        type_name,
        match def.category {
            Category::Types => "TLObject",
            Category::Functions => "TLRequest",
        },
    )?;

    write!(file, "{indent}        (Self {{")?;
    if def.params.len() != 0 {
        writeln!(file)?;
    }
    for param in def.params.iter() {
        match &param.ty {
            ParameterType::Flags => {
                // Flags are computed on-the-fly, not stored
            }
            ParameterType::Normal { .. } => {
                let attr_name = rustifier::parameters::attr_name(param);
                writeln!(file, "{}            {},", indent, attr_name,)?;
            }
        }
    }
    if def.params.len() != 0 {
        write!(file, "{indent}        ")?;
    }
    writeln!(
        file,
        "}}, crate::{} {{}})",
        match def.category {
            Category::Types => "TLObject",
            Category::Functions => "TLRequest",
        },
    )?;
    writeln!(file, "{indent}    }}")?;
    
    // to_bytes
    writeln!(
      file, 
      r#"{indent}    #[pyo3(name = "to_bytes")]
{indent}    fn py_to_bytes(&self) -> Vec<u8> {{
{indent}        use crate::Serializable;
{indent}        self.to_bytes()
{indent}    }}
"#,
    )?;
    // to_dict
    writeln!(
        file,
        "{indent}    fn to_dict(&self) -> pyo3::PyResult<pyo3::Py<pyo3::types::PyDict>> {{"
    )?;
    writeln!(file, "{indent}        pyo3::Python::attach(|py| {{")?;
    writeln!(file, "{indent}            use pyo3::types::PyDictMethods;")?;
    writeln!(
        file,
        "{indent}            let dict = pyo3::types::PyDict::new(py);"
    )?;
    writeln!(
        file,
        "{indent}            dict.set_item(\"_\", \"{}\")?;",
        type_name,
    )?;
    for param in def.params.iter() {
        match &param.ty {
            ParameterType::Flags => {
                // Flags are computed on-the-fly, not stored
            }
            ParameterType::Normal { .. } => {
                let attr_name = rustifier::parameters::attr_name(param);
                writeln!(
                    file,
                    "{indent}            dict.set_item(\"{name}\", self.{name}.clone())?;",
                    name = attr_name,
                )?;
            }
        }
    }
    writeln!(file, "{indent}            Ok(dict.into())")?;
    writeln!(file, "{indent}        }})")?;
    writeln!(file, "{indent}    }}")?;

    writeln!(file, "{indent}}}")?;
    Ok(())
}

/// Defines the `impl Identifiable` corresponding to the definition:
///
/// ```ignore
/// impl crate::Identifiable for PyName {
///     const CONSTRUCTOR_ID: u32 = 123;
/// }
/// ```
fn write_identifiable<W: Write>(file: &mut W, indent: &str, def: &Definition) -> io::Result<()> {
    writeln!(
        file,
        r#"{indent}impl crate::Identifiable for Py{} {{
{indent}    const CONSTRUCTOR_ID: u32 = {};
{indent}}}"#,
        rustifier::definitions::type_name(def),
        def.id
    )?;
    Ok(())
}

/// Defines the `impl Serializable` corresponding to the definition:
///
/// ```ignore
/// impl crate::Serializable for PyName {
///     fn serialize(&self, buf: &mut impl Extend<u8>) {
///         self.field.serialize(buf);
///     }
/// }
/// ```
fn write_serializable<W: Write>(file: &mut W, indent: &str, def: &Definition) -> io::Result<()> {
    let type_name = rustifier::definitions::type_name(def);
    writeln!(
        file,
        "{indent}impl crate::Serializable for Py{} {{",
        type_name,
    )?;
    writeln!(
        file,
        "{indent}    fn serialize(&self, {}buf: &mut impl Extend<u8>) {{",
        if def.params.is_empty() && def.category == Category::Types {
            "_"
        } else {
            ""
        },
    )?;

    match def.category {
        Category::Types => {
            // Bare types should not write their `CONSTRUCTOR_ID`.
        }
        Category::Functions => {
            // Functions should always write their `CONSTRUCTOR_ID`.
            // writeln!(file, "{indent}        use crate::Identifiable;")?;
            writeln!(file, "{indent}        Self::CONSTRUCTOR_ID.serialize(buf);")?;
        }
    }

    for param in def.params.iter() {
        write!(file, "{indent}        ")?;
        match &param.ty {
            ParameterType::Flags => {
                write!(file, "(0u32")?;

                // Compute flags as a single expression
                for p in def.params.iter() {
                    match &p.ty {
                        ParameterType::Normal {
                            ty,
                            flag: Some(flag),
                        } if flag.name == param.name => {
                            // We make sure this `p` uses the flag we're currently
                            // parsing by comparing (`p`'s) `flag.name == param.name`.

                            // OR (if the flag is present) the correct bit index.
                            // Only the special-cased "true" flags are booleans.
                            write!(
                                file,
                                " | if self.{}{} {{ {} }} else {{ 0 }}",
                                rustifier::parameters::attr_name(p),
                                if ty.name == "true" { "" } else { ".is_some()" },
                                1 << flag.index
                            )?;
                        }
                        _ => {}
                    }
                }

                writeln!(file, ").serialize(buf);")?;
            }
            ParameterType::Normal { ty, flag } => {
                // The `true` bare type is a bit special: it's empty so there
                // is not need to serialize it, but it's used enough to deserve
                // a special case and ignore it.
                if ty.name != "true" {
                    if flag.is_some() {
                        writeln!(
                            file,
                            "if let Some(ref x) = self.{} {{ ",
                            rustifier::parameters::attr_name(param)
                        )?;
                        writeln!(file, "{indent}            x.serialize(buf);")?;
                        writeln!(file, "{indent}        }}")?;
                    } else {
                        writeln!(
                            file,
                            "self.{}.serialize(buf);",
                            rustifier::parameters::attr_name(param)
                        )?;
                    }
                }
            }
        }
    }

    writeln!(file, "{indent}    }}")?;
    writeln!(file, "{indent}}}")?;

    // wrapper
    writeln!(
        file,
        r#"{indent}impl crate::Serializable for Py{}Wrapper {{
{indent}    fn serialize(&self, buf: &mut impl Extend<u8>) {{
{indent}        pyo3::Python::attach(|py| self.0.borrow(py).serialize(buf));
{indent}    }}
{indent}}}"#,
        type_name,
    )?;

    Ok(())
}

/// Defines the `impl Deserializable` corresponding to the definition:
///
/// ```ignore
/// impl crate::Deserializable for PyName {
///     fn deserialize(buf: crate::deserialize::Buffer) -> crate::deserialize::Result<Self> {
///         let field = FieldType::deserialize(buf)?;
///         Ok(Name { field })
///     }
/// }
/// ```
fn write_deserializable<W: Write>(
    file: &mut W,
    indent: &str,
    def: &Definition,
    metadata: &Metadata,
) -> io::Result<()> {
    let type_name = rustifier::definitions::type_name(def);
    writeln!(
        file,
        "{}impl crate::Deserializable for Py{} {{",
        indent, type_name,
    )?;
    writeln!(
        file,
        "{}    fn deserialize({}buf: crate::Buffer) -> crate::deserialize::Result<Self> {{",
        indent,
        if def.params.is_empty() { "_" } else { "" }
    )?;

    for param in def.params.iter() {
        write!(file, "{indent}        ")?;
        match &param.ty {
            ParameterType::Flags => {
                writeln!(
                    file,
                    "let {}{} = u32::deserialize(buf)?;",
                    if metadata.is_unused_flag(def, param) {
                        "_"
                    } else {
                        ""
                    },
                    rustifier::parameters::attr_name(param)
                )?;
            }
            ParameterType::Normal { ty, flag } => {
                if ty.name == "true" {
                    let flag = flag
                        .as_ref()
                        .expect("the `true` type must always be used in a flag");
                    writeln!(
                        file,
                        "let {} = ({} & {}) != 0;",
                        rustifier::parameters::attr_name(param),
                        flag.name,
                        1 << flag.index
                    )?;
                } else {
                    write!(file, "let {} = ", rustifier::parameters::attr_name(param))?;
                    if let Some(flag) = flag {
                        writeln!(file, "if ({} & {}) != 0 {{", flag.name, 1 << flag.index)?;
                        write!(file, "{indent}            Some(")?;
                    }
                    if ty.generic_ref {
                        write!(file, "{}::deserialize(buf)?", ty.name)?;
                    } else {
                        write!(
                            file,
                            "{}::deserialize(buf)?",
                            rustifier::types::item_path(ty)
                        )?;
                    }
                    if flag.is_some() {
                        writeln!(file, ")")?;
                        writeln!(file, "{indent}        }} else {{")?;
                        writeln!(file, "{indent}            None")?;
                        write!(file, "{indent}        }}")?;
                    }
                    writeln!(file, ";")?;
                }
            }
        }
    }

    writeln!(
        file,
        "{}        Ok(Py{} {{",
        indent,
        rustifier::definitions::type_name(def)
    )?;

    for param in def.params.iter() {
        match &param.ty {
            ParameterType::Flags => {}
            ParameterType::Normal { .. } => {
                writeln!(
                    file,
                    "{indent}            {},",
                    rustifier::parameters::attr_name(param)
                )?;
            }
        }
    }
    writeln!(file, "{indent}        }})")?;
    writeln!(file, "{indent}    }}")?;
    writeln!(file, "{indent}}}")?;

    // wrapper
    writeln!(
        file,
        r#"{indent}impl crate::Deserializable for Py{name}Wrapper {{
{indent}    fn deserialize(buf: crate::Buffer) -> crate::deserialize::Result<Self> {{
{indent}        Ok(Py{name}::deserialize(buf)?.into())
{indent}    }}
{indent}}}"#,
        name = type_name,
    )?;

    Ok(())
}

/// Writes an entire definition as Rust code (`struct` and `impl`).
fn write_definition<'a, W: Write>(
    file: &'a mut W,
    file_: &'a mut W,
    indent: &str,
    def: &Definition,
    metadata: &Metadata,
) -> io::Result<()> {
    write_struct(file, file_, indent, def)?;
    write_impl(file, indent, def)?;
    write_identifiable(file, indent, def)?;
    write_serializable(file, indent, def)?;

    if def.category == Category::Types
    // special-case needed for update handling
    || def.name == "sendMessage"
    {
        write_deserializable(file, indent, def, metadata)?;
    }
    writeln!(file)?;
    Ok(())
}

pub fn write_category_mod<'a, W: Write>(
    mut file: &'a mut W,
    mut file_: &'a mut W,
    category: Category,
    definitions: &[Definition],
    metadata: &Metadata,
) -> io::Result<()> {
    let cat = match category {
        Category::Functions => "functions",
        Category::Types => "types",
    };
    writeln!(file, "pub mod {} {{", cat)?;
    writeln!(file_, "#[pyo3::pymodule(name = \"{}\")]", cat)?;
    writeln!(file_, "pub mod {}_ {{", cat)?;

    let grouped = grouper::group_by_ns(definitions, category);
    let mut sorted_keys: Vec<&String> = grouped.keys().collect();
    sorted_keys.sort();

    for key in sorted_keys.into_iter() {
        // Begin possibly inner mod
        let indent = if key.is_empty() {
            "    "
        } else {
            writeln!(file, "    pub mod {key} {{")?;
            writeln!(file_, "    #[pyo3::pymodule]")?;
            writeln!(file_, "    pub mod {key} {{")?;
            "        "
        };

        for definition in grouped[key]
            .iter()
            .filter(|def| def.category == Category::Functions || !ignore_type(&def.ty))
        {
            write_definition(&mut file, &mut file_, indent, definition, metadata)?;
        }

        // End possibly inner mod
        if !key.is_empty() {
            writeln!(file, "    }}\n")?;
            writeln!(file_, "    }}\n")?;
        }
    }

    writeln!(file, "}}")?;
    writeln!(file_, "}}")?;
    Ok(())
}
