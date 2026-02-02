use std::sync::{Arc, Mutex};

use grammers_session::updates::UpdatesLike;
use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;
use pyo3_async_runtimes::tokio::get_runtime;

use tokio::sync::{mpsc, oneshot};
use tokio::task::JoinHandle;

use super::UpdateStream;
use crate::peer::PyUser;
use grammers_mtsender_pyo3::{ConnectionParams, SenderPool, SenderPoolFatHandle};
use grammers_session_pyo3::{PySession, Session};

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
    pub(crate) pool_task: Option<JoinHandle<()>>,
    pub(crate) updates: Option<mpsc::UnboundedReceiver<UpdatesLike>>,
    pub(crate) stream_updates: Option<UpdateStream>,
    pub(crate) handle: SenderPoolFatHandle,

    pub(crate) session: Session,
    pub(crate) api_id: i32,
    pub(crate) api_hash: String,
    pub(crate) bot_token: Option<String>,
    pub(crate) use_ipv6: bool,
    pub(crate) system_lang_code: String,
    pub(crate) lang_code: String,

    pub(crate) phone: Py<PyAny>,
    pub(crate) code: Py<PyAny>,
    pub(crate) password: Py<PyAny>,

    pub(crate) me: Option<Py<PyUser>>,
}

#[derive(Clone)]
#[pyclass(name = "Client", module = "grammers", subclass, dict)]
pub struct PyClient {
    pub inner: Arc<Mutex<ClientInner>>,
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
        app_version=None,
        device_model=None,
        system_version=None,
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
        bot_token: Option<&str>,
        app_version: Option<&str>,
        device_model: Option<&str>,
        system_version: Option<&str>,
        lang_code: Option<&str>,
        system_lang_code: Option<&str>,
        use_ipv6: bool,
    ) -> PyResult<Self> {
        let (loop_tx, loop_rx) = oneshot::channel::<Py<PyAny>>();
        let session = if session.is_instance_of::<PySession>() {
            Session::new(session.unbind(), loop_rx)
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
            device_model,
            system_version,
            app_version,
            system_lang_code: system_lang_code.clone(),
            lang_code: lang_code.clone(),
            proxy_url: None,
            __non_exhaustive: (),
        };

        let pool = SenderPool::new(session.clone(), api_id.0, config);
        let SenderPool {
            runner,
            updates,
            handle,
        } = pool;
        let pool_task = get_runtime().spawn(runner.run(loop_tx));

        let inner = ClientInner {
            pool_task: Some(pool_task),
            updates: Some(updates),
            stream_updates: None,
            handle,
            session: session,
            api_id: api_id.0,
            api_hash: api_hash.to_string(),
            phone,
            code,
            password,
            bot_token: bot_token.map(|x| x.to_string()),
            use_ipv6,
            system_lang_code: system_lang_code.to_string(),
            lang_code: lang_code.to_string(),
            me: None,
        };
        Ok(Self {
            inner: Arc::new(Mutex::new(inner)),
        })
    }

    #[getter]
    pub fn api_id(&self) -> i32 {
        self.inner.lock().unwrap().api_id
    }

    #[getter]
    pub fn api_hash(&self) -> String {
        self.inner.lock().unwrap().api_hash.clone()
    }

    #[getter]
    pub fn bot_token(&self) -> Option<String> {
        self.inner.lock().unwrap().bot_token.clone()
    }

    #[getter]
    pub fn use_ipv6(&self) -> bool {
        self.inner.lock().unwrap().use_ipv6
    }

    #[getter]
    pub fn system_lang_code(&self) -> String {
        self.inner.lock().unwrap().system_lang_code.clone()
    }

    #[getter]
    pub fn lang_code(&self) -> String {
        self.inner.lock().unwrap().lang_code.clone()
    }

    #[getter(session)]
    fn get_session(&self) -> Py<PyAny> {
        self.inner.lock().unwrap().session.get_inner()
    }

    #[getter]
    pub fn phone(&self) -> Py<PyAny> {
        Python::attach(|py| self.inner.lock().unwrap().phone.bind(py).clone().unbind())
    }

    #[getter]
    pub fn code(&self) -> Py<PyAny> {
        Python::attach(|py| self.inner.lock().unwrap().code.bind(py).clone().unbind())
    }

    #[getter]
    pub fn password(&self) -> Py<PyAny> {
        Python::attach(|py| {
            self.inner
                .lock()
                .unwrap()
                .password
                .bind(py)
                .clone()
                .unbind()
        })
    }

    #[getter(me)]
    fn _me(&self) -> Option<Py<PyUser>> {
        match &self.inner.lock().unwrap().me {
            None => None,
            Some(me) => Some(Python::attach(|py| me.bind(py).clone().unbind())),
        }
    }

    #[setter(me)]
    pub fn set_me(&self, user: Py<PyUser>) {
        self.inner.lock().unwrap().me = Some(user);
    }
}

impl PyClient {
    pub fn session(&self) -> Session {
        self.inner.lock().unwrap().session.clone()
    }

    pub fn handle(&self) -> SenderPoolFatHandle {
        self.inner.lock().unwrap().handle.clone()
    }
}
