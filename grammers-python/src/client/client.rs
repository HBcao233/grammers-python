use std::sync::{Arc, Mutex};

use grammers_session::updates::UpdatesLike;
use grammers_tl_types_pyo3 as pytl;
use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::PyString;
use pyo3_async_runtimes::tokio::get_runtime;

use tokio::sync::mpsc;
use tokio::sync::oneshot;
use tokio::task::JoinHandle;

use super::UpdateStream;
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
    pub pool_task: Option<JoinHandle<()>>,
    pub updates: Option<mpsc::UnboundedReceiver<UpdatesLike>>,
    pub stream_updates: Option<UpdateStream>,
    pub handle: SenderPoolFatHandle,

    pub session: Session,
    pub api_id: i32,
    pub api_hash: String,
    pub bot_token: Option<String>,
    use_ipv6: bool,
    system_lang_code: String,
    lang_code: String,
}

#[derive(Clone)]
#[pyclass(name = "Client", module = "grammers", subclass)]
pub struct PyClient {
    pub inner: Arc<Mutex<ClientInner>>,

    #[pyo3(get)]
    pub me: Option<pytl::enums::PyUser>,
}

#[pymethods]
impl PyClient {
    /// Create client instanse.
    ///
    /// Args:
    ///     session (``str`` | ``Session``):
    ///         A name for the client or a Session instanse.
    ///         E.g.: "my_account", SqliteSession("path").
    ///
    ///     api_id (``int`` | ``str``, *optional*):
    ///         The *api_id* part of the Telegram API key, as integer or string.
    ///         E.g.: 12345 or "12345".
    ///
    ///     api_hash (``str``, *optional*):
    ///         The *api_hash* part of the Telegram API key, as string.
    ///         E.g.: "0123456789abcdef0123456789abcdef".
    #[new]
    #[pyo3(signature = (
        session,
        api_id,
        api_hash,
        *,
        bot_token=None,
        app_version=None,
        device_model=None,
        system_version=None,
        lang_code="en",
        system_lang_code="en",
        use_ipv6=false,
    ))]
    pub fn new<'py>(
        py: pyo3::Python<'py>,
        session: Bound<'_, PyAny>,
        api_id: ApiId,
        api_hash: &str,
        // *,
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
        let info = os_info::get();
        let platform = py.import("platform")?;

        let device_model = match device_model {
            Some(x) => x.to_string(),
            None => {
                let os_type = format!("{}", info.os_type());
                let os_type: &str = os_type.as_str();
                let bitness = format!("{}", info.bitness());
                let bitness: &str = bitness.as_str();

                let implementation: Bound<'py, PyAny> = platform
                    .call_method0("python_implementation")
                    .unwrap_or(PyString::new(py, os_type).into_any());
                let implementation = implementation
                    .extract::<String>()
                    .unwrap_or(os_type.to_string());

                let version: Bound<'py, PyAny> = platform
                    .call_method0("python_implementation")
                    .unwrap_or(PyString::new(py, bitness).into_any());
                let version = version.extract::<String>().unwrap_or(bitness.to_string());
                format!("{} {}", implementation, version)
            }
        };
        let system_version = match system_version {
            Some(x) => x.to_string(),
            None => {
                let v = format!("{}", info.version());
                let v: &str = v.as_str();
                let system: Bound<'py, PyAny> = platform
                    .call_method0("system")
                    .unwrap_or(PyString::new(py, v).into_any());
                let system = system.extract::<String>().unwrap_or(v.to_string());

                let release: Bound<'py, PyAny> = platform
                    .call_method0("release")
                    .unwrap_or(PyString::new(py, "").into_any());
                let release = release.extract::<String>().unwrap_or("".to_string());
                format!("{} {}", system, release)
            }
        };
        let app_version = match app_version {
            Some(x) => x.to_string(),
            None => format!("Grammers {}", env!("CARGO_PKG_VERSION")),
        };

        let lang_code = match lang_code {
            Some(x) => x.to_string(),
            #[cfg(not(target_os = "android"))]
            None => locate_locale::user(),
            #[cfg(target_os = "android")]
            None => "en".to_string(),
        }
        .to_ascii_lowercase();
        let system_lang_code = match system_lang_code {
            Some(x) => x.to_string(),
            #[cfg(not(target_os = "android"))]
            None => locate_locale::system(),
            #[cfg(target_os = "android")]
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
        
        let pool = SenderPool::new(
            session.clone(), 
            api_id.0, 
            config,
        );
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
            // name: name.to_string(),
            api_id: api_id.0,
            api_hash: api_hash.to_string(),
            bot_token: bot_token.map(|x| x.to_string()),
            use_ipv6,
            system_lang_code: system_lang_code.to_string(),
            lang_code: lang_code.to_string(),
        };
        Ok(Self {
            inner: Arc::new(Mutex::new(inner)),
            me: None,
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
}
