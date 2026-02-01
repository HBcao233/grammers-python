// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

//! Several functions to "rustify" names.
//!
//! Each parsed type can have a corresponding "rusty" name, and
//! the method for it can be found in the corresponding submodule:
//!
//! * `type_name` for use after a type definition (`type FooBar`, `enum FooBar`).
//! * `qual_name` for the qualified type name (`crate::foo::BarBaz`).
//! * `variant_name` for use inside `enum` variants (`Foo`).
//! * `item_path` for use as a qualified item path (`Vec::<u8>`).
//! * `attr_name` for use as an attribute name (`foo_bar: ()`).

use std::fmt;

use crate::Metadata;

use grammers_tl_parser::tl::{Category, Definition, Parameter, ParameterType, Type};

/// Get the rusty type name for a certain definition, excluding namespace.
///
/// For example, transforms `"ns.some_OK_name"` into `"SomeOkName"`.
fn rusty_type_name(name: &str) -> String {
    enum Casing {
        Upper,
        Lower,
        Preserve,
    }

    let name = if let Some(pos) = name.rfind('.') {
        &name[pos + 1..]
    } else {
        name
    };

    let mut result = String::with_capacity(name.len());

    name.chars().fold(Casing::Upper, |casing, c| {
        if c == '_' {
            return Casing::Upper;
        }

        match casing {
            Casing::Upper => {
                result.push(c.to_ascii_uppercase());
                Casing::Lower
            }
            Casing::Lower => {
                result.push(c.to_ascii_lowercase());
                if c.is_ascii_uppercase() {
                    Casing::Lower
                } else {
                    Casing::Preserve
                }
            }
            Casing::Preserve => {
                result.push(c);
                if c.is_ascii_uppercase() {
                    Casing::Lower
                } else {
                    Casing::Preserve
                }
            }
        }
    });

    result
}

pub mod definitions {
    use super::*;

    pub fn type_name(def: &Definition) -> String {
        rusty_type_name(&def.name)
    }

    pub fn ns_type_name(def: &Definition) -> String {
        let mut result = String::new();
        def.namespace.iter().for_each(|ns| {
            result.push_str(ns);
            result.push_str("_");
        });
        result.push_str(&type_name(def));
        result
    }

    pub fn qual_name(def: &Definition) -> String {
        let mut result = String::new();
        result.push_str("crate::types::");
        def.namespace.iter().for_each(|ns| {
            result.push_str(ns);
            result.push_str("::");
        });
        result.push_str("Py");
        result.push_str(&type_name(def));
        result
    }

    pub fn wrap_qual_name(def: &Definition) -> String {
        let mut result = qual_name(def);
        result.push_str("Wrapper");
        result
    }

    pub fn tl_qual_name(def: &Definition) -> String {
        let mut result = String::new();
        result.push_str("grammers_tl_types::");
        result.push_str(match def.category {
            Category::Types => "types::",
            Category::Functions => "functions::",
        });
        def.namespace.iter().for_each(|ns| {
            result.push_str(ns);
            result.push_str("::");
        });
        result.push_str(&type_name(def));
        result
    }

    pub fn variant_name(def: &Definition) -> String {
        let name = type_name(def);
        let ty_name = types::type_name(&def.ty);

        let variant = if name.starts_with(&ty_name) {
            &name[ty_name.len()..]
        } else {
            &name
        };

        match variant {
            "Self" => {
                // Use the name from the second-to-last uppercase letter
                &name[name
                    .as_bytes()
                    .iter()
                    .take(name.len() - variant.len())
                    .rposition(|c| c.is_ascii_uppercase())
                    .unwrap_or(0)..]
            }
            // Note: this intentionally handles the empty string case too.
            _ if variant.chars().all(char::is_numeric) => {
                // Use the name from the last uppercase letter
                &name[name
                    .as_bytes()
                    .iter()
                    .rposition(|c| c.is_ascii_uppercase())
                    .unwrap_or(0)..]
            }
            _ => variant,
        }
        .to_string()
    }
}

pub mod functions {
    use super::*;

    pub fn qual_name(def: &Definition) -> String {
        let mut result = String::new();
        result.push_str("crate::functions::");
        def.namespace.iter().for_each(|ns| {
            result.push_str(ns);
            result.push_str("::");
        });
        result.push_str("Py");
        result.push_str(&definitions::type_name(def));
        result
    }

    pub fn wrap_qual_name(def: &Definition) -> String {
        let mut result = qual_name(def);
        result.push_str("Wrapper");
        result
    }
}

pub struct TypeNameFmt<'t>(pub &'t Type);

impl<'t> fmt::Display for TypeNameFmt<'t> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for ns in self.0.namespace.iter() {
            write!(f, "{}.", ns)?;
        }
        write!(f, "{}", self.0.name)
    }
}

pub mod types {
    use super::*;

    fn builtin_type(ty: &Type, path: bool) -> Option<&'static str> {
        Some(match ty.name.as_ref() {
            "Bool" => "bool",
            "bytes" => {
                if path {
                    "Vec::<u8>"
                } else {
                    "Vec<u8>"
                }
            }
            "double" => "f64",
            "int" => "i32",
            "int128" => {
                if path {
                    "<[u8; 16]>"
                } else {
                    "[u8; 16]"
                }
            }
            "int256" => {
                if path {
                    "<[u8; 32]>"
                } else {
                    "[u8; 32]"
                }
            }
            "long" => "i64",
            "string" => "String",
            "true" => "bool",
            "vector" => match type_name(&ty.generic_arg.as_ref().unwrap()).as_ref() {
                "IpPort" => "crate::PyRawVec_enums_IpPort",
                "FutureSalt" => "crate::PyRawVec_types_FutureSalt",
                "TlsBlock" => "crate::PyRawVec_enums_TlsBlock",
                "AccessPointRule" => "crate::PyRawVec_enums_AccessPointRule",
                _ => unreachable!(),
            },
            "Vector" => "Vec",
            _ => return None,
        })
    }

    // There are only minor differences between qualified
    // name and item paths so this method is used for both:
    // 1. use `::<...>` instead of `<...>` to specify type arguments
    // 2. missing angle brackets in associated item path
    fn get_path(ty: &Type, path: bool, obj: bool) -> String {
        if ty.generic_ref {
            // return ty.name.clone();
            return if obj {
                "crate::TLObjectLike"
            } else {
                "crate::TLRequestLike"
            }.to_string();
        }

        let btype = builtin_type(ty, path);
        let mut result = if let Some(name) = btype {
            name.to_string()
        } else {
            let mut result = String::new();
            result.push_str("crate");
            if ty.bare {
                result.push_str("::types::");
            } else {
                result.push_str("::enums::");
            }
            ty.namespace.iter().for_each(|ns| {
                result.push_str(ns);
                result.push_str("::");
            });

            result.push_str("Py");
            result.push_str(&type_name(ty));
            result
        };

        if let Some(generic_ty) = &ty.generic_arg {
            if ty.name != "vector".to_string() {
                if path {
                    result.push_str("::");
                }
                result.push('<');
                result.push_str(&get_path(generic_ty, path, obj));
                result.push('>');
            }
        }

        result
    }

    pub fn type_name(ty: &Type) -> String {
        rusty_type_name(&ty.name)
    }

    pub fn qual_name(ty: &Type) -> String {
        get_path(ty, false, false)
    }
    
    pub fn qual_name_obj(ty: &Type) -> String {
        get_path(ty, false, true)
    }

    pub fn item_path(ty: &Type) -> String {
        get_path(ty, true, false)
    }

    fn py_builtin_type(ty: &Type) -> Option<&'static str> {
        Some(match ty.name.as_ref() {
            "Bool" => "bool",
            "bytes" => "bytes",
            "double" => "float",
            "int" => "int",
            "int128" => "int",
            "int256" => "int",
            "long" => "int",
            "string" => "str",
            "true" => "bool",
            "vector" => "Sequence",
            "Vector" => "Sequence",
            _ => return None,
        })
    }

    pub fn py_qual_name(ty: &Type, metadata: &Metadata) -> String {
        if ty.generic_ref {
            // return ty.name.clone();
            return "TLRequest".to_string();
        }

        let btype = py_builtin_type(ty);
        let mut result = if let Some(name) = btype {
            name.to_string()
        } else {
            let mut result = String::new();
            if ty.bare {
                result.push_str("types.");
                ty.namespace.iter().for_each(|ns| {
                    result.push_str(ns);
                    result.push_str(".");
                });
                result.push_str(&type_name(ty));
            } else {
                let res = metadata
                    .defs_with_type(ty)
                    .iter()
                    .map(|d| {
                        let mut res = String::new();
                        res.push_str("types.");
                        d.namespace.iter().for_each(|ns| {
                            res.push_str(ns);
                            res.push_str(".");
                        });
                        res.push_str(&definitions::type_name(d));
                        res
                    })
                    .collect::<Vec<String>>()
                    .join(" | ");
                result.push_str(&res);
            }

            result
        };

        if let Some(generic_ty) = &ty.generic_arg {
            result.push('[');
            result.push_str(&py_qual_name(generic_ty, metadata));
            result.push(']');
        }

        result
    }

    fn builtin_into(ty: &Type) -> Option<&'static str> {
        Some(match ty.name.as_ref() {
            "Vector" => "v.into_iter().map(Into::into).collect()",
            _ => return None,
        })
    }

    pub fn get_into(ty: &Type) -> String {
        if ty.generic_ref {
            return "crate::TLRequestLike".to_string();
        }

        let result = match builtin_into(ty) {
            Some(v) => v.to_string(),
            None => "v.into()".to_string(),
        };
        /*
        let btype =
        let mut result = if let Some(name) = btype {
            name.to_string()
        } else {
            let mut result = String::new();
            result.push_str("crate");
            if ty.bare {
                result.push_str("::types::");
            } else {
                result.push_str("::enums::");
            }
            ty.namespace.iter().for_each(|ns| {
                result.push_str(ns);
                result.push_str("::");
            });

            result.push_str("Py");
            result.push_str(&type_name(ty));
            result
        };

        if let Some(generic_ty) = &ty.generic_arg {
            if btype.is_none() || btype != Some("crate::PyRawVec") {
                if path {
                    result.push_str("::");
                }
                result.push('<');
                result.push_str(&get_path(generic_ty, path));
                result.push('>');
            }
        }
        */

        result
    }
}

pub mod enums {
    use super::*;

    pub fn tl_qual_name(ty: &Type) -> String {
        let mut result = String::new();
        result.push_str("grammers_tl_types::enums::");
        ty.namespace.iter().for_each(|ns| {
            result.push_str(ns);
            result.push_str("::");
        });
        result.push_str(&rusty_type_name(&ty.name));
        result
    }
}

pub mod parameters {
    use super::*;

    pub fn qual_name(param: &Parameter) -> String {
        match &param.ty {
            ParameterType::Flags => "u32".into(),
            ParameterType::Normal { ty, flag } if flag.is_some() && ty.name == "true" => {
                "bool".into()
            }
            ParameterType::Normal { ty, flag } => {
                let mut result = String::new();
                if flag.is_some() {
                    result.push_str("Option<");
                }
                result.push_str(&types::qual_name(ty));
                if flag.is_some() {
                    result.push('>');
                }
                result
            }
        }
    }

    pub fn py_qual_name(param: &Parameter, metadata: &Metadata) -> String {
        match &param.ty {
            ParameterType::Flags => "bool".into(),
            ParameterType::Normal { ty, flag } if flag.is_some() && ty.name == "true" => {
                "bool".into()
            }
            ParameterType::Normal { ty, flag } => {
                let mut result = String::new();
                if flag.is_some() {
                    result.push_str("Optional[");
                }
                result.push_str(&types::py_qual_name(ty, metadata));
                if flag.is_some() {
                    result.push(']');
                }
                result
            }
        }
    }

    pub fn attr_name(param: &Parameter) -> String {
        match &param.name[..] {
            "final" => "r#final".into(),
            "loop" => "r#loop".into(),
            "self" => "is_self".into(),
            "static" => "r#static".into(),
            "type" => "r#type".into(),
            _ => {
                let mut result = param.name.clone();
                result[..].make_ascii_lowercase();
                result
            }
        }
    }

    pub fn py_attr_name(param: &Parameter) -> String {
        match &param.name[..] {
            "final" => "final".into(),
            "loop" => "loop".into(),
            "self" => "is_self".into(),
            "static" => "static".into(),
            "type" => "type".into(),
            "from" => "_from".into(),
            _ => {
                let mut result = param.name.clone();
                result[..].make_ascii_lowercase();
                result
            }
        }
    }
}
