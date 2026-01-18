use grammers_tl_types as tl;
use pyo3::exceptions::PyNotImplementedError;
use pyo3::prelude::*;
use pyo3::types::PyDict;
use pyo3::{Bound, FromPyObject, IntoPyObject, Py, PyAny, Python};

pub type Buffer<'a, 'b> = &'a mut grammers_tl_types::deserialize::Cursor<'b>;

#[cfg_attr(feature = "stub-gen", pyo3_stub_gen::derive::gen_stub_pyclass)]
#[repr(transparent)]
#[derive(Debug, Clone)]
#[pyclass]
pub struct PyRawVec(Vec<crate::PyTLObject>);

impl tl::Serializable for PyRawVec {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        (self.0.len() as i32).serialize(buf);
        self.0.iter().for_each(|x| x.serialize(buf));
    }
}
impl tl::Deserializable for PyRawVec {
    fn deserialize(buf: crate::Buffer) -> tl::deserialize::Result<Self> {
        let len = u32::deserialize(buf)?;
        Ok(Self(
            (0..len)
                .map(|_| crate::PyTLObject::deserialize(buf))
                .collect::<tl::deserialize::Result<Vec<crate::PyTLObject>>>()?,
        ))
    }
}

#[cfg_attr(feature = "stub-gen", pyo3_stub_gen::derive::gen_stub_pyclass)]
#[derive(Debug, Clone, PartialEq)]
#[pyclass(module = "grammers.tl", subclass)]
pub struct TLObject {}

#[cfg_attr(feature = "stub-gen", pyo3_stub_gen::derive::gen_stub_pymethods)]
#[pymethods]
impl TLObject {
    #[staticmethod]
    #[pyo3(signature = (obj, indent=Some(0)))]
    fn pretty_format(obj: Bound<'_, PyAny>, indent: Option<usize>) -> PyResult<String> {
        let (obj, cls_name) = if obj.is_instance_of::<TLObject>() {
            let cls = obj.getattr("__class__")?;
            let cls_name: String = cls.getattr("__name__")?.extract()?;
            (obj.call_method0("to_dict")?, cls_name)
        } else {
            (obj, "TLObject".to_string())
        };
        let d = if let Ok(dict) = obj.cast::<PyDict>() {
            dict
        } else {
            return Ok(obj.repr()?.to_string());
        };

        let indent = indent.unwrap_or(0);
        let class_name = match d.get_item("_")? {
            Some(x) => x.extract::<String>()?,
            None => cls_name,
        };

        // 获取所有非"_"的键值对
        let mut attrs: Vec<(String, Bound<'_, PyAny>)> = Vec::new();
        for (key, value) in d.iter() {
            if let Ok(key_str) = key.extract::<String>() {
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

        let current_indent = "  ".repeat(indent + 1);
        let closing_indent = "  ".repeat(indent);

        for (key, value) in attrs {
            let formatted_value = TLObject::pretty_format(value, Some(indent + 1))?;
            result.push_str(&format!("{}{}={},\n", current_indent, key, formatted_value));
        }

        result.push_str(&format!("{})", closing_indent));
        Ok(result)
    }

    fn __repr__(slf: Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf.clone().into_any(), None)
    }

    fn __eq__(&self, other: Bound<'_, PyAny>) -> PyResult<bool> {
        let other = if other.is_instance_of::<TLObject>() {
            other.call_method0("to_dict")?
        } else {
            return Ok(false);
        };
        let dict = self.to_dict()?;
        let result: bool = Python::attach(|py| {
            let dict: Bound<'_, PyAny> = dict.into_bound(py).into_any();
            let result: Bound<'_, PyAny> = dict.call_method1("__eq__", (other,))?;
            result.extract()
        })?;
        Ok(result)
    }

    fn to_json(&self) -> PyResult<String> {
        let data = self.to_dict()?;
        let result: String = Python::attach(|py| {
            let cls = Bound::new(py, self.clone())?
                .into_any()
                .getattr("__class__")?;
            let cls_name = cls.getattr("__name__")?;
            data.call_method1(py, "setdefault", ("_", cls_name))?;
            let data: Bound<'_, PyAny> = data.into_bound(py).into_any();
            let json = py.import("json")?;
            let kwargs = PyDict::new(py);
            kwargs.set_item("ensure_ascii", false)?;
            let result: Bound<'_, PyAny> = json.call_method("dumps", (data,), Some(&kwargs))?;
            result.extract()
        })?;
        Ok(result)
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

#[cfg_attr(feature = "stub-gen", pyo3_stub_gen::derive::gen_stub_pyclass)]
#[pyclass(module = "grammers.tl", subclass)]
#[derive(Debug, Clone, PartialEq)]
pub struct TLRequest {}

#[cfg_attr(feature = "stub-gen", pyo3_stub_gen::derive::gen_stub_pymethods)]
#[pymethods]
impl TLRequest {
    #[staticmethod]
    #[pyo3(signature = (obj, indent=Some(0)))]
    fn pretty_format(obj: Bound<'_, PyAny>, indent: Option<usize>) -> PyResult<String> {
        TLObject::pretty_format(obj, indent)
    }

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Err(PyNotImplementedError::new_err(
            "TLObject subclasses must implement to_dict()",
        ))
    }
}

#[repr(transparent)]
#[derive(Debug, Clone, FromPyObject, IntoPyObject)]
pub struct PyTLObjectWrapper(crate::PyTLObject);

#[cfg(feature = "stub-gen")]
impl pyo3_stub_gen::PyStubType for PyTLObjectWrapper {
    fn type_output() -> pyo3_stub_gen::TypeInfo {
        pyo3_stub_gen::TypeInfo {
            name: "grammers.tl.TLObject".to_string(),
            import: vec!["grammers.tl".into()].into_iter().collect(),
        }
    }
}
impl tl::Serializable for PyTLObjectWrapper {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        self.0.serialize(buf);
    }
}
impl tl::Deserializable for PyTLObjectWrapper {
    fn deserialize(buf: crate::Buffer) -> tl::deserialize::Result<Self> {
        let x = crate::PyTLObject::deserialize(buf)?;
        Ok(Self(x))
    }
}

#[repr(transparent)]
#[derive(Debug, Clone, FromPyObject, IntoPyObject)]
pub struct PyTLRequestWrapper(crate::PyTLRequest);

#[cfg(feature = "stub-gen")]
impl pyo3_stub_gen::PyStubType for PyTLRequestWrapper {
    fn type_output() -> pyo3_stub_gen::TypeInfo {
        pyo3_stub_gen::TypeInfo {
            name: "grammers.tl.TLRequest".to_string(),
            import: vec!["grammers.tl".into()].into_iter().collect(),
        }
    }
}
impl tl::Serializable for PyTLRequestWrapper {
    fn serialize(&self, buf: &mut impl Extend<u8>) {
        self.0.serialize(buf);
    }
}
