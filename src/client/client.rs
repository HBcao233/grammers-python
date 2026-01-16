use pyo3::prelude::*;
use pyo3::exceptions::{PyRuntimeError, PyTypeError, PyValueError};
use pyo3::types::PyString;
use pyo3_async_runtimes::tokio::get_runtime;
use std::sync::Arc;
use grammers_client::{Client, SenderPool};
use grammers_session::storages::SqliteSession;
use grammers_session::updates::UpdatesLike;
use grammers_mtsender::{ConnectionParams, SenderPoolHandle};
use tokio::sync::mpsc;
use tokio::task::JoinHandle;

#[cfg(feature = "stub-gen")]
use pyo3_stub_gen::derive::*;


#[derive(Debug, Clone)]
pub struct ApiId(pub i32);

impl<'a, 'py> FromPyObject<'a, 'py> for ApiId {
  type Error = PyErr;
  
  fn extract(ob: Borrowed<'a, 'py, PyAny>) -> Result<Self, Self::Error> {
    if let Ok(val) = ob.extract::<i32>() {
      return Ok(ApiId(val));
    }
    if let Ok(s) = ob.extract::<String>() {
      return s.parse::<i32>()
        .map(ApiId)
        .map_err(|e| PyErr::new::<PyValueError, _>(
          format!("Cannot convert '{}' to int: {}", s, e)
        ));
    }
    Err(PyErr::new::<PyTypeError, _>(
      "api_id must be int or str"
    ))
  }
}


#[cfg_attr(feature = "stub-gen", gen_stub_pyclass)]
#[pyclass(name = "Client", module = "grammers", subclass)]
pub struct PyClient {
  pub inner: Client,
  pub pool_task: Option<JoinHandle<()>>,
  pub updates: mpsc::UnboundedReceiver<UpdatesLike>,
  pub handle: SenderPoolHandle,
  
  #[pyo3(get)]
  name: String,
  
  #[pyo3(get)]
  pub api_id: i32,
  
  #[pyo3(get)]
  api_hash: String,
  
  #[pyo3(get)]
  bot_token: Option<String>,
  
  #[pyo3(get)]
  use_ipv6: bool,
  
  #[pyo3(get)]
  system_lang_code: String,
  
  #[pyo3(get)]
  lang_code: String,
}

#[cfg_attr(feature = "stub-gen", gen_stub_pymethods)]
#[pymethods]
impl PyClient {
  /// Create instanse
  /// 
  /// Args:
  ///     name (``str``):
  ///         A name for the client, e.g.: "my_account".
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
    name,
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
    name: &str,
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
    let info = os_info::get();
    let platform = py.import("platform")?;
    
    let device_model = match device_model {
      Some(x) => x.to_string(),
      None => {
        let os_type = format!("{}", info.os_type());
        let os_type: &str = os_type.as_str();
        let bitness = format!("{}", info.bitness());
        let bitness: &str = bitness.as_str();
        
        let implementation: Bound<'py, PyAny> = platform.call_method0("python_implementation").unwrap_or(
          PyString::new(py, os_type).into_any()
        );
        let implementation = implementation.extract::<String>().unwrap_or(os_type.to_string());
        
        let version: Bound<'py, PyAny> = platform.call_method0("python_implementation").unwrap_or(
          PyString::new(py, bitness).into_any()
        );
        let version = version.extract::<String>().unwrap_or(bitness.to_string());
        format!("{} {}", implementation, version)
      }
    };
    let system_version = match system_version {
      Some(x) => x.to_string(),
      None => {
        let v = format!("{}", info.version());
        let v: &str = v.as_str();
        let system: Bound<'py, PyAny> = platform.call_method0("system").unwrap_or(
          PyString::new(py, v).into_any()
        );
        let system = system.extract::<String>().unwrap_or(v.to_string());
        
        let release: Bound<'py, PyAny> = platform.call_method0("release").unwrap_or(
          PyString::new(py, "").into_any()
        );
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
      None => "en".to_string(),
    }.to_ascii_lowercase();
    let system_lang_code = match system_lang_code {
      Some(x) => x.to_string(),
      None => "en".to_string(),
    }.to_ascii_lowercase();
    
    let config = ConnectionParams {
      device_model,
      system_version,
      app_version,
      system_lang_code: system_lang_code.clone(),
      lang_code: lang_code.clone(),
      proxy_url: None,
      __non_exhaustive: (),
    };
    let session = Arc::new(
      SqliteSession::open(
        name.to_owned() + ".session"
      ).map_err(|e: rusqlite::Error| {
        PyRuntimeError::new_err(e.to_string())
      })?
    );
    let pool = SenderPool::with_configuration(
      Arc::clone(&session), 
      api_id.0,
      config,
    );
    let inner = Client::new(&pool);
    let SenderPool {
      runner,
      updates,
      handle,
    } = pool;
    let pool_task = get_runtime().spawn(runner.run());

    Ok(Self {
      inner,
      updates,
      handle,
      pool_task: Some(pool_task),
      name: name.to_string(),
      api_id: api_id.0, 
      api_hash: api_hash.to_string(),
      bot_token: bot_token.map(|x| x.to_string()),
      use_ipv6,
      system_lang_code: system_lang_code.to_string(),
      lang_code: lang_code.to_string(),
    })
  }
}
