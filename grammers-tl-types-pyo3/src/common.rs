use pyo3::exceptions::PyNotImplementedError;
use pyo3::prelude::*;
use pyo3::exceptions::PyTypeError;
use pyo3::types::{PyString, PyBytes, PyDict, PyMapping, PySequence};

use grammers_tl_types as tl;

static FORMAT_INDENT: &'static str = "    ";

#[allow(non_camel_case_types)]
#[repr(transparent)]
#[derive(Debug, Clone)]
#[pyclass]
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
#[pyclass]
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
#[pyclass]
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
#[pyclass]
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
#[pyclass(module = "grammers.tl", subclass)]
pub struct TLObject {}

#[pymethods]
impl TLObject {
    #[staticmethod]
    #[pyo3(signature = (obj, indent))]
    pub fn pretty_format(obj: &Bound<'_, PyAny>, indent: Option<usize>) -> PyResult<String> {
        if indent.is_some() && indent > Some(20) {
            return Ok("...".to_string());
        }
        
        let d;
        let (obj, cls_name) = if obj.is_instance_of::<TLObject>() {
            let cls_name = obj.get_type().qualname()?;
            d = obj.call_method0("to_dict")?;
            (&d, cls_name.extract()?)
        } else {
            (obj, "TLObject".to_string())
        };
        
        let next_indent = match indent {
            None => None,
            Some(x) => Some(x + 1),
        };
        let current_indent = match indent {
            None => "",
            Some(x) => &FORMAT_INDENT.repeat(x + 1),
        };
        let closing_indent = match indent {
            None => "",
            Some(x) => &FORMAT_INDENT.repeat(x),
        };
        let newline_or_empty = match indent {
            None => "",
            Some(_) => "\n",
        };
        let comma_newline_or_space = match indent {
            None => ", ",
            Some(_) => ",\n",
        };

        let result = if let Ok(dict) = obj.cast::<PyMapping>() {
            let class_name = match dict.get_item("_") {
                Err(_) => cls_name,
                Ok(x) => x.extract().unwrap_or(cls_name),
            };

            let mut attrs: Vec<(String, Bound<'_, PyAny>)> = Vec::new();
            let keys = dict.keys()?;
            for key in keys.iter() {
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

            let result = attrs.iter()
                .map(|(key, value)| {
                    let value = TLObject::pretty_format(&value, next_indent)?;
                    let value = if key == "phone" {
                        crate::utils::mask_phone(&value)
                    } else {
                        value
                    };
                    Ok(format!(
                        "{}{}={}",
                        current_indent,
                        key,
                        value,
                    ))
                })
                .collect::<PyResult<Vec<String>>>()?
                .join(comma_newline_or_space) + newline_or_empty;

            format!(
                "{}({}{}{})",
                class_name,
                newline_or_empty,
                result,
                closing_indent,
            )
        } else if obj.is_instance_of::<PyString>() {
            obj.repr()?.to_string()
        } else if let Ok(seq) = obj.cast::<PySequence>() {
            let len = seq.len()?;
            if len == 0 {
                return Ok("[]".to_string());
            }

            let result = (0..len)
                .map(|i| {
                    let value = seq.get_item(i)?;
                    let value = TLObject::pretty_format(&value, next_indent)?;
                    Ok(format!(
                        "{}{}",
                        current_indent,
                        value,
                    ))
                })
                .collect::<PyResult<Vec<String>>>()?
                .join(comma_newline_or_space) + newline_or_empty;

            format!(
                "[{}{}{}]", 
                newline_or_empty,
                result,
                closing_indent
            )
        } else {
            obj.repr()?.to_string()
        };
        
        Ok(result)
    }

    fn __str__(slf: &Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf, Some(0))
    }

    fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf, None)
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
        if obj.is_instance_of::<PyBytes>() {
            return Ok(obj.repr()?.into_any().unbind());
        }
        if obj.is_instance_of::<TLObject>() || obj.is_instance_of::<TLRequest>() {
            return Ok(obj.call_method0("to_dict")?.unbind());
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

#[pyclass(module = "grammers.tl", subclass)]
#[derive(Debug, Clone, PartialEq)]
pub struct TLRequest {}

#[pymethods]
impl TLRequest {
    fn __str__(slf: &Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf, Some(0))
    }
    
    fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf, None)
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
