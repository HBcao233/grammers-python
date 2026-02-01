use pyo3::exceptions::PyNotImplementedError;
use pyo3::prelude::*;
use pyo3::types::{PyDict, PyMapping, PySequence};
use pyo3::{Bound, Py, PyAny};

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
    #[pyo3(signature = (obj, indent=Some(0)))]
    pub fn pretty_format(obj: &Bound<'_, PyAny>, indent: Option<usize>) -> PyResult<String> {
        let _d;
        let (d, cls_name) = if obj.is_instance_of::<TLObject>() {
            let cls_name = obj.get_type().qualname()?;
            _d = obj.call_method0("to_dict")?;
            (&_d, cls_name.extract()?)
        } else {
            (obj, "TLObject".to_string())
        };
        
        let indent = indent.unwrap_or(0);
        Ok(if let Ok(dict) = d.cast::<PyMapping>() {
            let class_name = match dict.get_item("_") {
                Err(_) => cls_name,
                Ok(x) => x.extract().unwrap_or(cls_name),
            };
    
            // 获取所有非"_"的键值对
            let mut attrs: Vec<(String, Bound<'_, PyAny>)> = Vec::new();
            for key in dict.keys()? {
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
            result.push_str(&format!("{}(\n", class_name));
    
            let current_indent = FORMAT_INDENT.repeat(indent + 1);
            let closing_indent = FORMAT_INDENT.repeat(indent);
    
            for (key, value) in attrs {
                let value = TLObject::pretty_format(&value, Some(indent + 1))?;
                let value = if key == "phone" {
                    crate::utils::mask_phone(&value)
                } else {
                    value
                };
                result.push_str(&format!("{}{}={},\n", current_indent, key, value));
            }
    
            result.push_str(&format!("{})", closing_indent));
            result
        } else if let Ok(seq) = d.cast::<PySequence>() {
            let mut result = String::new();
            result.push_str("[\n");

            let current_indent = FORMAT_INDENT.repeat(indent + 1);
            let closing_indent = FORMAT_INDENT.repeat(indent);

            for value in seq.to_list()?.iter() {
                let value = TLObject::pretty_format(&value, Some(indent + 1))?;
                result.push_str(&format!("{}{},\n", current_indent, value));
            }
            result.push_str(&format!("{}]", closing_indent));
            result
        } else {
            obj.repr()?.to_string()
        })
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

    fn to_json(slf: &Bound<'_, Self>) -> PyResult<String> {
        let py = slf.py();

        let data = slf.call_method0("to_dict")?;
        let cls_name = slf.get_type().qualname()?;
        data.call_method1("setdefault", ("_", cls_name))?;

        let json = py.import("json")?;
        let kwargs = PyDict::new(py);
        kwargs.set_item("ensure_ascii", false)?;
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
    fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf, None)
    }

    fn __eq__(self_: Bound<'_, Self>, other: &Bound<'_, PyAny>) -> PyResult<bool> {
        let other = if other.is_instance_of::<TLRequest>() {
            other.call_method0("to_dict")?
        } else {
            return Ok(false);
        };
        let dict = self_.call_method0("to_dict")?;
        let result = dict.call_method1("__eq__", (other,))?;

        Ok(result.extract()?)
    }

    fn to_json(self_: &Bound<'_, Self>) -> PyResult<String> {
        let py = self_.py();

        let data = self_.call_method0("to_dict")?;
        let cls_name = self_.get_type().qualname()?;
        data.call_method1("setdefault", ("_", cls_name))?;

        let json = py.import("json")?;
        let kwargs = PyDict::new(py);
        kwargs.set_item("ensure_ascii", false)?;
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
