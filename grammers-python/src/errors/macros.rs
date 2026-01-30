/// macros to create rpc errors.

macro_rules! createInvalidDCError {
    ($struct_name:ident, $py_name:literal, $message_template:literal) => {
        #[pyclass(name = $py_name, module = "grammers.errors", extends = PyInvalidDCError)]
        pub struct $struct_name {}

        #[pymethods]
        impl $struct_name {
            #[new]
            #[pyo3(signature = (name, value, caused_by = None))]
            fn new(
                name: String,
                value: Option<u32>,
                caused_by: Option<u32>,
            ) -> PyClassInitializer<Self> {
                let template = $message_template;
                let message = if template.contains("{}") && value.is_some() {
                    template.replace("{}", &value.unwrap().to_string())
                } else {
                    template.to_string()
                };
                PyClassInitializer::from(PyRpcError {
                    code: 303,
                    name,
                    value,
                    caused_by,
                    message: Some(message),
                })
                .add_subclass(PyInvalidDCError {})
                .add_subclass($struct_name {})
            }
        }

        impl $struct_name {
            pub fn new_err(name: String, value: Option<u32>, caused_by: Option<u32>) -> PyErr {
                PyErr::new::<$struct_name, _>((name, value, caused_by))
            }
        }
    };
}

macro_rules! createBadRequestError {
    ($struct_name:ident, $py_name:literal, $message_template:literal) => {
        #[pyclass(name = $py_name, module = "grammers.errors", extends = PyBadRequestError)]
        pub struct $struct_name {}

        #[pymethods]
        impl $struct_name {
            #[new]
            #[pyo3(signature = (name, value, caused_by = None))]
            fn new(
                name: String,
                value: Option<u32>,
                caused_by: Option<u32>,
            ) -> PyClassInitializer<Self> {
                let template = $message_template;
                let message = if template.contains("{}") && value.is_some() {
                    template.replace("{}", &value.unwrap().to_string())
                } else {
                    template.to_string()
                };
                PyClassInitializer::from(PyRpcError {
                    code: 400,
                    name: name,
                    value,
                    caused_by,
                    message: Some(message),
                })
                .add_subclass(PyBadRequestError {})
                .add_subclass($struct_name {})
            }
        }

        impl $struct_name {
            pub fn new_err(name: String, value: Option<u32>, caused_by: Option<u32>) -> PyErr {
                PyErr::new::<$struct_name, _>((name, value, caused_by))
            }
        }
    };
}

macro_rules! createUnauthorizedError {
    ($struct_name:ident, $py_name:literal, $message_template:literal) => {
        #[pyclass(name = $py_name, module = "grammers.errors", extends = PyUnauthorizedError)]
        pub struct $struct_name {}

        #[pymethods]
        impl $struct_name {
            #[new]
            #[pyo3(signature = (name, value, caused_by = None))]
            fn new(
                name: String,
                value: Option<u32>,
                caused_by: Option<u32>,
            ) -> PyClassInitializer<Self> {
                let template = $message_template;
                let message = if template.contains("{}") && value.is_some() {
                    template.replace("{}", &value.unwrap().to_string())
                } else {
                    template.to_string()
                };
                PyClassInitializer::from(PyRpcError {
                    code: 401,
                    name: name,
                    value,
                    caused_by,
                    message: Some(message),
                })
                .add_subclass(PyUnauthorizedError {})
                .add_subclass($struct_name {})
            }
        }

        impl $struct_name {
            pub fn new_err(name: String, value: Option<u32>, caused_by: Option<u32>) -> PyErr {
                PyErr::new::<$struct_name, _>((name, value, caused_by))
            }
        }
    };
}

macro_rules! createForbiddenError {
    ($struct_name:ident, $py_name:literal, $message_template:literal) => {
        #[pyclass(name = $py_name, module = "grammers.errors", extends = PyForbiddenError)]
        pub struct $struct_name {}

        #[pymethods]
        impl $struct_name {
            #[new]
            #[pyo3(signature = (name, value, caused_by = None))]
            fn new(
                name: String,
                value: Option<u32>,
                caused_by: Option<u32>,
            ) -> PyClassInitializer<Self> {
                let template = $message_template;
                let message = if template.contains("{}") && value.is_some() {
                    template.replace("{}", &value.unwrap().to_string())
                } else {
                    template.to_string()
                };
                PyClassInitializer::from(PyRpcError {
                    code: 403,
                    name: name,
                    value,
                    caused_by,
                    message: Some(message),
                })
                .add_subclass(PyForbiddenError {})
                .add_subclass($struct_name {})
            }
        }

        impl $struct_name {
            pub fn new_err(name: String, value: Option<u32>, caused_by: Option<u32>) -> PyErr {
                PyErr::new::<$struct_name, _>((name, value, caused_by))
            }
        }
    };
}

macro_rules! createAuthKeyError {
    ($struct_name:ident, $py_name:literal, $message_template:literal) => {
        #[pyclass(name = $py_name, module = "grammers.errors", extends = PyAuthKeyError)]
        pub struct $struct_name {}

        #[pymethods]
        impl $struct_name {
            #[new]
            #[pyo3(signature = (name, value, caused_by = None))]
            fn new(
                name: String,
                value: Option<u32>,
                caused_by: Option<u32>,
            ) -> PyClassInitializer<Self> {
                let template = $message_template;
                let message = if template.contains("{}") && value.is_some() {
                    template.replace("{}", &value.unwrap().to_string())
                } else {
                    template.to_string()
                };
                PyClassInitializer::from(PyRpcError {
                    code: 406,
                    name: name,
                    value,
                    caused_by,
                    message: Some(message),
                })
                .add_subclass(PyAuthKeyError {})
                .add_subclass($struct_name {})
            }
        }

        impl $struct_name {
            pub fn new_err(name: String, value: Option<u32>, caused_by: Option<u32>) -> PyErr {
                PyErr::new::<$struct_name, _>((name, value, caused_by))
            }
        }
    };
}

macro_rules! createFloodError {
    ($struct_name:ident, $py_name:literal, $message_template:literal) => {
        #[pyclass(name = $py_name, module = "grammers.errors", extends = PyFloodError)]
        pub struct $struct_name {}

        #[pymethods]
        impl $struct_name {
            #[new]
            #[pyo3(signature = (name, value, caused_by = None))]
            fn new(
                name: String,
                value: Option<u32>,
                caused_by: Option<u32>,
            ) -> PyClassInitializer<Self> {
                let template = $message_template;
                let message = if template.contains("{}") && value.is_some() {
                    template.replace("{}", &value.unwrap().to_string())
                } else {
                    template.to_string()
                };
                PyClassInitializer::from(PyRpcError {
                    code: 420,
                    name,
                    value,
                    caused_by,
                    message: Some(message),
                })
                .add_subclass(PyFloodError {})
                .add_subclass($struct_name {})
            }
        }

        impl $struct_name {
            pub fn new_err(name: String, value: Option<u32>, caused_by: Option<u32>) -> PyErr {
                PyErr::new::<$struct_name, _>((name, value, caused_by))
            }
        }
    };
}

macro_rules! createServerError {
    ($struct_name:ident, $py_name:literal, $message_template:literal) => {
        #[pyclass(name = $py_name, module = "grammers.errors", extends = PyServerError)]
        pub struct $struct_name {}

        #[pymethods]
        impl $struct_name {
            #[new]
            #[pyo3(signature = (name, value, caused_by = None))]
            fn new(
                name: String,
                value: Option<u32>,
                caused_by: Option<u32>,
            ) -> PyClassInitializer<Self> {
                let template = $message_template;
                let message = if template.contains("{}") && value.is_some() {
                    template.replace("{}", &value.unwrap().to_string())
                } else {
                    template.to_string()
                };
                PyClassInitializer::from(PyRpcError {
                    code: 500,
                    name,
                    value,
                    caused_by,
                    message: Some(message),
                })
                .add_subclass(PyServerError {})
                .add_subclass($struct_name {})
            }
        }

        impl $struct_name {
            pub fn new_err(name: String, value: Option<u32>, caused_by: Option<u32>) -> PyErr {
                PyErr::new::<$struct_name, _>((name, value, caused_by))
            }
        }
    };
}

pub(crate) use createAuthKeyError;
pub(crate) use createBadRequestError;
pub(crate) use createFloodError;
pub(crate) use createForbiddenError;
pub(crate) use createInvalidDCError;
pub(crate) use createServerError;
pub(crate) use createUnauthorizedError;
