use pyo3::prelude::*;
use pyo3::types::PyType;
use pyo3::exceptions::{PyTypeError, PyNotImplementedError};
use pyo3_async_runtimes::tokio::into_future;
use super::{PyDcOption, PyPeerId, PeerIdLike, PyPeerInfo, PyPeerRef, PyUpdatesState, PyUpdateState};

#[derive(Clone)]
#[pyclass(
    name = "Session",
    module = "grammers.sessions",
    subclass
)]
pub struct PySession {}

#[pymethods]
impl PySession {
    #[new]
    fn new() -> Self {
        Self {}
    }
    
    #[classmethod]
    fn __init_subclass__(cls: &Bound<'_, PyType>) -> PyResult<()> {
        let cls_dict = cls.getattr("__dict__")?;
        let required_methods = [
            "home_dc_id", "set_home_dc_id",
            "dc_option", "set_home_dc_id", 
            "peer", "cache_peer",
            "updates_state", "set_update_state"
        ];
        for method in required_methods {
            if !cls_dict.contains(method)? {
                return Err(PyTypeError::new_err(
                    format!(
                        "Can't instantiate abstract class {} without an implementation for abstract method '{}'",
                        cls.name()?,
                        method,
                    )
                ))
            }
        }
        Ok(())
    }
    
    async fn home_dc_id(&self) -> PyResult<i32> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement home_dc_id()",
        ))
    }
    
    #[allow(unused_variables)]
    #[pyo3(signature = (dc_id))]
    async fn set_home_dc_id(&self, dc_id: i32) -> PyResult<()> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement set_home_dc_id()",
        ))
    }
    
    #[allow(unused_variables)]
    #[pyo3(signature = (dc_id))]
    async fn dc_option(&self, dc_id: i32) -> PyResult<Option<PyDcOption>> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement dc_option()",
        ))
    }
    
    #[allow(unused_variables)]
    #[pyo3(signature = (dc_option))]
    async fn set_dc_option(&self, dc_option: Py<PyDcOption>) -> PyResult<()> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement set_dc_option()",
        ))
    }
    
    #[allow(unused_variables)]
    #[pyo3(signature = (peer))]
    async fn peer(&self, peer: PeerIdLike) -> PyResult<Option<PyPeerInfo>> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement peer()",
        ))
    }
    
    #[allow(unused_variables)]
    #[pyo3(signature = (peer_info))]
    async fn cache_peer(&self, peer_info: Py<PyPeerInfo>) -> PyResult<()> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement cache_peer()",
        ))
    }
    
    #[pyo3(signature = ())]
    async fn updates_state(&self) -> PyResult<PyUpdatesState> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement updates_state()",
        ))
    }
    
    #[allow(unused_variables)]
    #[pyo3(signature = (update))]
    async fn set_update_state(&self, update: Py<PyUpdateState>) -> PyResult<()> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement set_update_state()",
        ))
    }
}


pub struct Session(pub Py<PyAny>);
impl Clone for Session {
    fn clone(&self) -> Self {
        Self(Python::attach(|py| self.0.bind(py).clone().into()))
    }
}
impl Session {
    pub async fn home_dc_id(&self) -> PyResult<i32> {
        let res = Python::attach(|py| {
            let coroutine = self.0.bind(py).call_method0("home_dc_id")?;
            into_future(coroutine)
        })?
        .await?;
        Python::attach(|py| {
            res.bind(py).extract::<i32>()
        })
    }
    
    pub async fn set_home_dc_id(&self, dc_id: i32) -> PyResult<()> {
        Python::attach(|py| {
            let coroutine = self.0.bind(py).call_method1("set_home_dc_id", (dc_id,))?;
            into_future(coroutine)
        })?.await?;
        Ok(())
    }
    
    pub async fn dc_option(&self, dc_id: i32) -> PyResult<Option<PyDcOption>> {
        let res = Python::attach(|py| {
            let coroutine = self.0.bind(py).call_method1("dc_option", (dc_id,))?;
            into_future(coroutine)
        })?.await?;
        Python::attach(|py| {
            let res = res.bind(py);
            Ok(if res.is_none() {
                None
            } else {
                Some(res.cast::<PyDcOption>()?.borrow().clone())
            })
        })
    }
    
    pub async fn set_dc_option(&self, dc_option: PyDcOption) -> PyResult<()> {
        Python::attach(|py| {
            let dc_option = Py::new(py, dc_option)?;
            let coroutine = self.0.bind(py).call_method1("set_dc_option", (dc_option,))?;
            into_future(coroutine)
        })?.await?;
        Ok(())
    }
    
    pub async fn peer(&self, peer: PyPeerId) -> PyResult<Option<PyPeerInfo>> {
        let res = Python::attach(|py| {
            let peer = Py::new(py, peer)?;
            let coroutine = self.0.bind(py).call_method1("peer", (peer,))?;
            into_future(coroutine)
        })?
        .await?;
        Python::attach(|py| {
            let res = res.bind(py);
            Ok(if res.is_none() {
              None
            } else {
              Some(res.cast::<PyPeerInfo>()?.borrow().clone())
            })
        })
    }
    
    pub async fn peer_ref(&self, peer: PyPeerId) -> PyResult<Option<PyPeerRef>> {
        Ok(self.peer(peer)
            .await?
            .and_then(|info| info.auth())
            .map(|auth| PyPeerRef { id: peer, auth }))
    }
    
    pub async fn cache_peer(&self, peer_info: PyPeerInfo) -> PyResult<()> {
        Python::attach(|py| {
            let peer_info = Py::new(py, peer_info)?;
            let coroutine = self.0.bind(py).call_method1("cache_peer", (peer_info,))?;
            into_future(coroutine)
        })?.await?;
        Ok(())
    }
    
    pub async fn updates_state(&self) -> PyResult<PyUpdatesState> {
        let res = Python::attach(|py| {
            let coroutine = self.0.bind(py).call_method0("updates_state")?;
            into_future(coroutine)
        })?.await?;
        Python::attach(|py| {
            Ok(res.bind(py).cast::<PyUpdatesState>()?.borrow().clone())
        })
    }
    
    pub async fn set_update_state(&self, update: PyUpdateState) -> PyResult<()> {
        Python::attach(|py| {
            let update = Py::new(py, update)?;
            let coroutine = self.0.bind(py).call_method1("set_update_state", (update,))?;
            into_future(coroutine)
        })?.await?;
        Ok(())
    }
}