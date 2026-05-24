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

use crate::Metadata;

use grammers_tl_parser::tl::{Definition, Parameter, ParameterType, Type};

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
}

pub mod types {
    use super::*;

    pub fn type_name(ty: &Type) -> String {
        rusty_type_name(&ty.name)
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
}

pub mod parameters {
    use super::*;

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
