use std::sync::{Arc, Mutex};

use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;

use tokio::sync::{Notify, mpsc};
use tokio::task::JoinHandle;

use grammers_mtsender_pyo3::{ConnectionParams, SenderPool, SenderPoolFatHandle};
use grammers_session::updates::UpdatesLike;
use grammers_session_pyo3::{PyPeerRef, PySession, Session};

use crate::events::{EventHandlersManager, EventPoolHandle};
use crate::peer::PyUser;
// use crate::runtime::RUNTIME;

#[derive(Debug, Clone)]
pub struct ApiId(pub i32);

impl<'a, 'py> FromPyObject<'a, 'py> for ApiId {
    type Error = PyErr;

    fn extract(ob: Borrowed<'a, 'py, PyAny>) -> Result<Self, Self::Error> {
        if let Ok(val) = ob.extract::<i32>() {
            return Ok(ApiId(val));
        }
        if let Ok(s) = ob.extract::<String>() {
            return s.parse::<i32>().map(ApiId).map_err(|e| {
                PyErr::new::<PyValueError, _>(format!("Cannot convert '{}' to int: {}", s, e))
            });
        }
        Err(PyTypeError::new_err("api_id must be int or str"))
    }
}

pub struct ClientInner {
    pub(crate) pool_task: Mutex<Option<JoinHandle<()>>>,
    pub(crate) updates: Mutex<Option<mpsc::UnboundedReceiver<UpdatesLike>>>,

    pub(crate) handle: SenderPoolFatHandle,

    pub(crate) event_handlers: EventHandlersManager,
    pub(crate) event_pool_handle: Mutex<Option<EventPoolHandle>>,
    pub(crate) event_pool_task: Mutex<Option<JoinHandle<PyResult<()>>>>,
    /// Signalled when the event pool runner finishes (for any reason).
    pub(crate) event_pool_done: Notify,

    pub(crate) session: Session,
    pub(crate) me: Mutex<Option<Py<PyUser>>>,

    // Readonly properties.
    pub(crate) api_id: i32,
    pub(crate) api_hash: String,
    pub(crate) bot_token: Option<String>,
    pub(crate) use_ipv6: bool,
    pub(crate) device_model: String,
    pub(crate) system_version: String,
    pub(crate) app_version: String,
    pub(crate) system_lang_code: String,
    pub(crate) lang_code: String,

    pub(crate) phone: Py<PyAny>,
    pub(crate) code: Py<PyAny>,
    pub(crate) password: Py<PyAny>,
}

#[derive(Clone)]
#[pyclass(from_py_object, name = "Client", module = "grammers", subclass, dict)]
pub struct PyClient {
    pub inner: Arc<ClientInner>,
}

#[pymethods]
impl PyClient {
    /// Create client instanse.
    #[new]
    #[pyo3(signature = (
        session,
        api_id,
        api_hash,
        *,
        phone,
        code,
        password,
        bot_token=None,
        device_model=None,
        system_version=None,
        app_version=None,
        lang_code=None,
        system_lang_code=None,
        use_ipv6=false,
    ))]
    pub fn new<'py>(
        py: pyo3::Python<'py>,
        session: Bound<'_, PyAny>,
        api_id: ApiId,
        api_hash: &str,
        // *,
        phone: Py<PyAny>,
        code: Py<PyAny>,
        password: Py<PyAny>,
        bot_token: Option<String>,
        device_model: Option<&str>,
        system_version: Option<&str>,
        app_version: Option<&str>,
        lang_code: Option<&str>,
        system_lang_code: Option<&str>,
        use_ipv6: bool,
    ) -> PyResult<Self> {
        let session = if session.is_instance_of::<PySession>() {
            Session::new(session.unbind())
        } else {
            let cls_name = session.get_type().qualname()?;
            return Err(PyTypeError::new_err(format!(
                "session expected a Session, got {}",
                cls_name
            )));
        };
        let platform = py.import("platform")?;

        let device_model = match device_model {
            Some(x) => x.to_string(),
            None => {
                let implementation = match platform.call_method0("python_implementation") {
                    Err(_) => "Python".to_string(),
                    Ok(x) => x.extract().unwrap_or("Python".to_string()),
                };
                let version = match platform.call_method0("python_version") {
                    Err(_) => "".to_string(),
                    Ok(x) => x.extract().unwrap_or("".to_string()),
                };
                format!("{} {}", implementation, version)
            }
        };
        let system_version = match system_version {
            Some(x) => x.to_string(),
            None => {
                let system = match platform.call_method0("system") {
                    Err(_) => "".to_string(),
                    Ok(x) => x.extract::<String>().unwrap_or("".to_string()),
                };
                let release = match platform.call_method0("release") {
                    Err(_) => "".to_string(),
                    Ok(x) => x.extract::<String>().unwrap_or("".to_string()),
                };
                format!("{} {}", system, release)
            }
        };
        let app_version = match app_version {
            Some(x) => x.to_string(),
            None => format!("Grammers {}", env!("CARGO_PKG_VERSION")),
        };

        let lang_code = match lang_code {
            Some(x) => x.to_string(),
            None => "en".to_string(),
        }
        .to_ascii_lowercase();
        let system_lang_code = match system_lang_code {
            Some(x) => x.to_string(),
            None => "en".to_string(),
        }
        .to_ascii_lowercase();

        let config = ConnectionParams {
            device_model: device_model.clone(),
            system_version: system_version.clone(),
            app_version: app_version.clone(),
            system_lang_code: system_lang_code.clone(),
            lang_code: lang_code.clone(),
            proxy_url: None,
            __non_exhaustive: (),
        };

        let pool =
            Python::attach(|py| SenderPool::new(py, session.clone_ref(py), api_id.0, config));
        let SenderPool {
            runner,
            updates,
            handle,
        } = pool;
        let pool_task = pyo3_async_runtimes::tokio::get_runtime().spawn(runner.run());

        let inner = ClientInner {
            pool_task: Mutex::new(Some(pool_task)),
            updates: Mutex::new(Some(updates)),
            handle,
            event_handlers: EventHandlersManager::new(),
            event_pool_handle: Mutex::new(None),
            event_pool_task: Mutex::new(None),
            event_pool_done: Notify::new(),
            session: session,
            api_id: api_id.0,
            api_hash: api_hash.to_string(),
            phone,
            code,
            password,
            bot_token: bot_token,
            use_ipv6,
            device_model,
            system_version,
            app_version,
            system_lang_code: system_lang_code.to_string(),
            lang_code: lang_code.to_string(),
            me: Mutex::new(None),
        };
        Ok(Self {
            inner: Arc::new(inner),
        })
    }

    #[getter]
    pub fn api_id(&self) -> i32 {
        self.inner.api_id
    }

    #[getter]
    pub fn api_hash(&self) -> String {
        self.inner.api_hash.clone()
    }

    #[getter]
    pub fn bot_token(&self) -> Option<String> {
        self.inner.bot_token.clone()
    }

    #[getter]
    pub fn use_ipv6(&self) -> bool {
        self.inner.use_ipv6
    }

    #[getter]
    pub fn device_model(&self) -> String {
        self.inner.device_model.clone()
    }

    #[getter]
    pub fn system_version(&self) -> String {
        self.inner.system_version.clone()
    }

    #[getter]
    pub fn app_version(&self) -> String {
        self.inner.app_version.clone()
    }

    #[getter]
    pub fn system_lang_code(&self) -> String {
        self.inner.system_lang_code.clone()
    }

    #[getter]
    pub fn lang_code(&self) -> String {
        self.inner.lang_code.clone()
    }

    #[getter(session)]
    fn get_session(&self) -> Py<PyAny> {
        let inner = self.inner.clone();
        Python::attach(|py| inner.session.get_inner(py))
    }

    #[getter]
    pub fn phone(&self) -> Py<PyAny> {
        Python::attach(|py| self.inner.phone.clone_ref(py))
    }

    #[getter]
    pub fn code(&self) -> Py<PyAny> {
        Python::attach(|py| self.inner.code.clone_ref(py))
    }

    #[getter]
    pub fn password(&self) -> Py<PyAny> {
        Python::attach(|py| self.inner.password.clone_ref(py))
    }

    #[getter(me)]
    pub fn _me(&self) -> Option<Py<PyUser>> {
        let inner = self.inner.clone();
        match inner.me.lock().unwrap().as_ref() {
            None => None,
            Some(me) => Some(Python::attach(|py| me.clone_ref(py))),
        }
    }
}

impl PyClient {
    pub fn me_ref(&self) -> PyResult<PyPeerRef> {
        let me = self._me();
        match me {
            Some(me) => {
                let (id, auth) = Python::attach(|py| {
                    let borrowed = me.borrow(py);
                    (borrowed.id(), borrowed.auth().unwrap_or_default())
                });
                Ok(PyPeerRef { id, auth })
            }
            None => Err(PyValueError::new_err("me must be cached")),
        }
    }

    pub fn set_me(&self, user: Py<PyUser>) {
        let inner = self.inner.clone();
        *inner.me.lock().unwrap() = Some(user);
    }
}
