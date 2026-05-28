use std::fmt::Write;

use pyo3::exceptions::PyNotImplementedError;
use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyDateTime, PyDict, PyMapping, PySequence, PyString};

use grammers_tl_types as tl;

static FORMAT_INDENT: &'static str = "\t";
const MAX_INDENT_DEPTH: usize = 20;

#[allow(non_camel_case_types)]
#[repr(transparent)]
#[derive(Debug, Clone)]
#[pyclass(from_py_object)]
pub struct PyRawVec_enums_IpPort(pub Vec<crate::enums::PyIpPort>);

impl tl::Serializable for PyRawVec_enums_IpPort {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        (self.0.len() as i32).serialize(buf);
        self.0.iter().for_each(|x| x.serialize(buf));
    }
}
impl tl::Deserializable for PyRawVec_enums_IpPort {
    fn deserialize(buf: crate::Buffer) -> tl::deserialize::Result<Self> {
        let len = u32::deserialize(buf)?;
        Ok(Self(
            (0..len)
                .map(|_| crate::enums::PyIpPort::deserialize(buf))
                .collect::<tl::deserialize::Result<Vec<crate::enums::PyIpPort>>>()?,
        ))
    }
}
impl<T: Into<crate::enums::PyIpPort>> From<tl::RawVec<T>> for PyRawVec_enums_IpPort {
    fn from(x: tl::RawVec<T>) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}
impl<T: From<crate::enums::PyIpPort>> From<PyRawVec_enums_IpPort> for tl::RawVec<T> {
    fn from(x: PyRawVec_enums_IpPort) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}

#[allow(non_camel_case_types)]
#[repr(transparent)]
#[derive(Debug, Clone)]
#[pyclass(from_py_object)]
pub struct PyRawVec_types_FutureSalt(pub Vec<crate::types::PyFutureSalt>);

impl tl::Serializable for PyRawVec_types_FutureSalt {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        (self.0.len() as i32).serialize(buf);
        self.0.iter().for_each(|x| x.serialize(buf));
    }
}
impl tl::Deserializable for PyRawVec_types_FutureSalt {
    fn deserialize(buf: crate::Buffer) -> tl::deserialize::Result<Self> {
        let len = u32::deserialize(buf)?;
        Ok(Self(
            (0..len)
                .map(|_| crate::types::PyFutureSalt::deserialize(buf))
                .collect::<tl::deserialize::Result<Vec<crate::types::PyFutureSalt>>>()?,
        ))
    }
}
impl<T: Into<crate::types::PyFutureSalt>> From<tl::RawVec<T>> for PyRawVec_types_FutureSalt {
    fn from(x: tl::RawVec<T>) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}
impl<T: From<crate::types::PyFutureSalt>> From<PyRawVec_types_FutureSalt> for tl::RawVec<T> {
    fn from(x: PyRawVec_types_FutureSalt) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}

#[allow(non_camel_case_types)]
#[repr(transparent)]
#[derive(Debug, Clone)]
#[pyclass(from_py_object)]
pub struct PyRawVec_enums_TlsBlock(pub Vec<crate::enums::PyTlsBlock>);

impl tl::Serializable for PyRawVec_enums_TlsBlock {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        (self.0.len() as i32).serialize(buf);
        self.0.iter().for_each(|x| x.serialize(buf));
    }
}
impl tl::Deserializable for PyRawVec_enums_TlsBlock {
    fn deserialize(buf: crate::Buffer) -> tl::deserialize::Result<Self> {
        let len = u32::deserialize(buf)?;
        Ok(Self(
            (0..len)
                .map(|_| crate::enums::PyTlsBlock::deserialize(buf))
                .collect::<tl::deserialize::Result<Vec<crate::enums::PyTlsBlock>>>()?,
        ))
    }
}
impl<T: Into<crate::enums::PyTlsBlock>> From<tl::RawVec<T>> for PyRawVec_enums_TlsBlock {
    fn from(x: tl::RawVec<T>) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}
impl<T: From<crate::enums::PyTlsBlock>> From<PyRawVec_enums_TlsBlock> for tl::RawVec<T> {
    fn from(x: PyRawVec_enums_TlsBlock) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}

#[allow(non_camel_case_types)]
#[repr(transparent)]
#[derive(Debug, Clone)]
#[pyclass(from_py_object)]
pub struct PyRawVec_enums_AccessPointRule(pub Vec<crate::enums::PyAccessPointRule>);

impl tl::Serializable for PyRawVec_enums_AccessPointRule {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        (self.0.len() as i32).serialize(buf);
        self.0.iter().for_each(|x| x.serialize(buf));
    }
}
impl tl::Deserializable for PyRawVec_enums_AccessPointRule {
    fn deserialize(buf: crate::Buffer) -> tl::deserialize::Result<Self> {
        let len = u32::deserialize(buf)?;
        Ok(Self(
            (0..len)
                .map(|_| crate::enums::PyAccessPointRule::deserialize(buf))
                .collect::<tl::deserialize::Result<Vec<crate::enums::PyAccessPointRule>>>()?,
        ))
    }
}
impl<T: Into<crate::enums::PyAccessPointRule>> From<tl::RawVec<T>>
    for PyRawVec_enums_AccessPointRule
{
    fn from(x: tl::RawVec<T>) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}
impl<T: From<crate::enums::PyAccessPointRule>> From<PyRawVec_enums_AccessPointRule>
    for tl::RawVec<T>
{
    fn from(x: PyRawVec_enums_AccessPointRule) -> Self {
        Self(x.0.into_iter().map(Into::into).collect())
    }
}

#[derive(Debug, Clone, PartialEq)]
#[pyclass(skip_from_py_object, module = "grammers.tl", subclass)]
pub struct TLObject {}

#[pymethods]
impl TLObject {
    #[staticmethod]
    #[pyo3(signature = (obj, indent))]
    pub fn pretty_format(obj: Bound<'_, PyAny>, indent: Option<usize>) -> PyResult<String> {
        if let Some(i) = indent {
            if i > MAX_INDENT_DEPTH {
                return Ok("...".to_string());
            }
        }

        let (next_indent, current_indent, closing_indent, newline_or_empty, comma_newline_or_space) =
            match indent {
                None => (
                    None,
                    String::new(),
                    String::new(),
                    String::new(),
                    ", ".to_string(),
                ),
                Some(x) => {
                    let current = FORMAT_INDENT.repeat(x + 1);
                    let closing = FORMAT_INDENT.repeat(x);
                    (
                        Some(x + 1),
                        current,
                        closing,
                        "\n".to_string(),
                        ",\n".to_string(),
                    )
                }
            };

        let cls_name = obj.get_type().qualname()?.to_string();
        let obj = match obj.getattr("to_dict") {
            Ok(to_dict) => to_dict.call0()?,
            Err(_) => obj,
        };

        if let Ok(dict) = obj.cast::<PyMapping>() {
            let class_name = dict
                .get_item("_")
                .ok()
                .and_then(|x| x.extract().ok())
                .unwrap_or(cls_name);

            let mut attrs: Vec<(String, Bound<'_, PyAny>)> = Vec::new();
            for key in dict.keys()?.iter() {
                if let Ok(key_str) = key.extract::<String>() {
                    let value = dict.get_item(key)?;
                    if key_str != "_" {
                        attrs.push((key_str, value));
                    }
                }
            }

            if attrs.is_empty() {
                return Ok(format!("{}()", class_name));
            }

            let mut result = String::new();
            for (i, (key, value)) in attrs.into_iter().enumerate() {
                if i > 0 {
                    result.push_str(&comma_newline_or_space);
                }

                let formatted_value = TLObject::pretty_format(value, next_indent)?;
                let formatted_value = if key == "phone" {
                    crate::utils::mask_phone(&formatted_value)
                } else {
                    formatted_value
                };

                write!(result, "{}{}={}", current_indent, key, formatted_value)
                    .expect("write to String failed");
            }

            result.push_str(&newline_or_empty);

            return Ok(format!(
                "{}({}{}{})",
                class_name, newline_or_empty, result, closing_indent,
            ));
        }

        if obj.is_instance_of::<PyBytes>() {
            return Ok(obj.repr()?.to_string());
        }

        if obj.is_instance_of::<PyString>() {
            return Ok(obj.repr()?.to_string());
        }

        if let Ok(seq) = obj.cast::<PySequence>() {
            let len = seq.len()?;
            if len == 0 {
                return Ok("[]".to_string());
            }

            let mut result = String::new();
            for i in 0..len {
                if i > 0 {
                    result.push_str(&comma_newline_or_space);
                }
                let value = seq.get_item(i)?;
                let formatted = TLObject::pretty_format(value, next_indent)?;
                use std::fmt::Write;
                write!(result, "{}{}", current_indent, formatted).expect("write to String failed");
            }
            result.push_str(&newline_or_empty);

            return Ok(format!(
                "[{}{}{}]",
                newline_or_empty, result, closing_indent
            ));
        }

        Ok(obj.repr()?.to_string())
    }

    fn __str__(slf: Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf.into_any(), Some(0))
    }

    fn __repr__(slf: Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf.into_any(), None)
    }

    fn __eq__(slf: &Bound<'_, Self>, other: &Bound<'_, PyAny>) -> PyResult<bool> {
        let other = if other.is_instance_of::<TLObject>() {
            other.call_method0("to_dict")?
        } else {
            return Ok(false);
        };
        let dict1 = slf.call_method0("to_dict")?;
        let dict2 = other.call_method0("to_dict")?;
        let result = dict1.call_method1("__eq__", (dict2,))?;

        Ok(result.extract()?)
    }

    #[staticmethod]
    fn json_default(obj: &Bound<'_, PyAny>) -> PyResult<Py<PyAny>> {
        let py = obj.py();
        if obj.is_instance_of::<PyBytes>() {
            let dict = PyDict::new(py);
            dict.set_item("_", "bytes")?;
            dict.set_item("__repr__", obj.str()?)?;
            return Ok(dict.unbind().into_any());
        }
        if let Ok(to_dict) = obj.getattr("to_dict") {
            return Ok(to_dict.call0()?.unbind());
        }
        if obj.is_instance_of::<PyDateTime>() {
            let dict = PyDict::new(py);
            dict.set_item("_", "datetime.datetime")?;
            dict.set_item("__repr__", obj.repr()?)?;
            return Ok(dict.unbind().into_any());
        }

        let cls_name = obj.get_type().qualname()?;
        Err(PyTypeError::new_err(format!(
            "Object of type {} is not JSON serializable",
            cls_name,
        )))
    }

    fn to_json(slf: &Bound<'_, Self>) -> PyResult<String> {
        let py = slf.py();

        let data = slf.call_method0("to_dict")?;
        let cls_name = slf.get_type().qualname()?;
        data.call_method1("setdefault", ("_", cls_name))?;

        let json = py.import("json")?;
        let kwargs = PyDict::new(py);
        kwargs.set_item("ensure_ascii", false)?;
        let default_fn = slf.getattr("json_default")?;
        kwargs.set_item("default", default_fn)?;

        let result: Bound<'_, PyAny> = json.call_method("dumps", (&data,), Some(&kwargs))?;

        Ok(result.extract()?)
    }

    fn to_bytes(&self) -> PyResult<Vec<u8>> {
        Err(PyNotImplementedError::new_err(
            "TLObject subclasses must implement to_bytes()",
        ))
    }

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Err(PyNotImplementedError::new_err(
            "TLObject subclasses must implement to_dict()",
        ))
    }
}

#[derive(Debug, Clone, PartialEq)]
#[pyclass(skip_from_py_object, module = "grammers.tl", subclass)]
pub struct TLRequest {}

#[pymethods]
impl TLRequest {
    fn __str__(slf: Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf.into_any(), Some(0))
    }

    fn __repr__(slf: Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf.into_any(), None)
    }

    fn __eq__(slf: Bound<'_, Self>, other: &Bound<'_, PyAny>) -> PyResult<bool> {
        let other = if other.is_instance_of::<TLRequest>() {
            other.call_method0("to_dict")?
        } else {
            return Ok(false);
        };
        let dict = slf.call_method0("to_dict")?;
        let result = dict.call_method1("__eq__", (other,))?;

        Ok(result.extract()?)
    }

    fn to_json(slf: &Bound<'_, Self>) -> PyResult<String> {
        let py = slf.py();

        let data = slf.call_method0("to_dict")?;
        let cls_name = slf.get_type().qualname()?;
        data.call_method1("setdefault", ("_", cls_name))?;

        let json = py.import("json")?;
        let kwargs = PyDict::new(py);
        kwargs.set_item("ensure_ascii", false)?;
        let default_fn = slf.getattr("json_default")?;
        kwargs.set_item("default", default_fn)?;

        let result: Bound<'_, PyAny> = json.call_method("dumps", (&data,), Some(&kwargs))?;

        Ok(result.extract()?)
    }

    fn to_bytes(&self) -> PyResult<Vec<u8>> {
        Err(PyNotImplementedError::new_err(
            "TLObject subclasses must implement to_bytes()",
        ))
    }

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Err(PyNotImplementedError::new_err(
            "TLObject subclasses must implement to_dict()",
        ))
    }
}
