use super::{
    PeerIdLike, PeerInfo, PyDcOption, PyPeerId, PyPeerInfo, PyPeerRef, PyUpdateState,
    PyUpdatesState, UpdateStateLike,
};
use pyo3::exceptions::{PyNotImplementedError, PyTypeError};
use pyo3::prelude::*;
use pyo3::types::PyType;

use std::sync::Arc;
use tokio::sync::Mutex;
use tokio::sync::OnceCell;
use tokio::sync::oneshot;

use crate::utils::into_future;

#[derive(Clone)]
#[pyclass(name = "Session", module = "grammers.sessions", subclass, dict)]
pub struct PySession {}

#[pymethods]
impl PySession {
    #[new]
    fn new() -> Self {
        Self {}
    }

    #[classmethod]
    fn __init_subclass__(cls: &Bound<'_, PyType>) -> PyResult<()> {
        let py = cls.py();
        let inspect = py.import("inspect")?;
        let cls_dict = cls.getattr("__dict__")?;
        let required_methods = [
            "close",
            "home_dc_id",
            "set_home_dc_id",
            "dc_option",
            "set_home_dc_id",
            "peer",
            "cache_peer",
            "updates_state",
            "set_update_state",
        ];

        for method in required_methods {
            if !cls_dict.contains(method)? {
                return Err(PyTypeError::new_err(format!(
                    "Can't instantiate abstract class {} without an implementation for abstract method '{}'",
                    cls.name()?,
                    method,
                )));
            }

            let func = cls.getattr(method)?;
            let is_coro = inspect
                .call_method1("iscoroutinefunction", (&func,))?
                .extract::<bool>()?;
            if !is_coro {
                return Err(PyTypeError::new_err(format!(
                    "Can't instantiate abstract class {}, because the implementation for abstract method '{}' is not a coroutine function (async def).",
                    cls.name()?,
                    method,
                )));
            }
        }
        Ok(())
    }

    async fn close(&self) -> PyResult<()> {
        Err(PyNotImplementedError::new_err(
            "Session subclasses must implement close()",
        ))
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
    async fn updates_state(&self) -> PyResult<Py<PyUpdatesState>> {
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

// For use on the Rust side
pub struct Session {
    inner: Py<PyAny>,
    event_loop: Arc<OnceCell<Py<PyAny>>>,
    loop_rx: Arc<Mutex<Option<oneshot::Receiver<Py<PyAny>>>>>,
}
impl Clone for Session {
    fn clone(&self) -> Self {
        Python::attach(|py| Self {
            inner: self.inner.bind(py).clone().unbind(),
            event_loop: self.event_loop.clone(),
            loop_rx: self.loop_rx.clone(),
        })
    }
}
impl Session {
    pub fn new(session: Py<PyAny>, loop_rx: oneshot::Receiver<Py<PyAny>>) -> Self {
        Self {
            inner: session,
            event_loop: Arc::new(OnceCell::new()),
            loop_rx: Arc::new(Mutex::new(Some(loop_rx))),
        }
    }

    pub fn get_inner<'py>(&self, py: Python<'py>) -> Py<PyAny> {
        Py::clone_ref(&self.inner, py)
    }

    pub fn cls_name<'py>(&self, py: Python<'py>) -> PyResult<String> {
        self.inner
            .bind(py)
            .get_type()
            .qualname()?
            .extract::<String>()
    }

    pub async fn event_loop(&self) -> &Py<PyAny> {
        self.event_loop
            .get_or_init(|| async { self.loop_rx.lock().await.take().unwrap().await.unwrap() })
            .await
    }

    pub async fn close(&self) -> PyResult<()> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            self.inner
                .bind(py)
                .call_method0("close")
                .map(|x| x.unbind())
        })?;
        into_future(event_loop, coro).await?;
        Ok(())
    }

    pub async fn home_dc_id(&self) -> PyResult<i32> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            self.inner
                .bind(py)
                .call_method0("home_dc_id")
                .map(|x| x.unbind())
        })?;
        let res = into_future(event_loop, coro).await?;
        Python::attach(|py| res.extract(py)).map_err(|e| {
            let cls_name = match Python::attach(|py| self.cls_name(py)) {
                Ok(name) => name,
                Err(e) => return e,
            };
            PyTypeError::new_err(format!("{}.home_dc_id(): {}", cls_name, e))
        })
    }

    pub async fn set_home_dc_id(&self, dc_id: i32) -> PyResult<()> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            self.inner
                .bind(py)
                .call_method1("set_home_dc_id", (dc_id,))
                .map(|x| x.unbind())
        })?;
        into_future(event_loop, coro).await?;
        Ok(())
    }

    pub async fn dc_option(&self, dc_id: i32) -> PyResult<Option<PyDcOption>> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            self.inner
                .bind(py)
                .call_method1("dc_option", (dc_id,))
                .map(|x| x.unbind())
        })?;
        let res = into_future(event_loop, coro).await?;
        Python::attach(|py| Ok::<_, PyErr>(res.extract(py)?)).map_err(|e| {
            let cls_name = match Python::attach(|py| self.cls_name(py)) {
                Ok(name) => name,
                Err(e) => return e,
            };
            PyTypeError::new_err(format!("{}.dc_option(): {}", cls_name, e))
        })
    }

    pub async fn set_dc_option(&self, dc_option: PyDcOption) -> PyResult<()> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            let dc_option = Py::new(py, dc_option)?;
            self.inner
                .bind(py)
                .call_method1("set_dc_option", (dc_option,))
                .map(|x| x.unbind())
        })?;
        into_future(event_loop, coro).await?;
        Ok(())
    }

    pub async fn peer(&self, peer: PyPeerId) -> PyResult<Option<PeerInfo>> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            let peer = Py::new(py, peer)?;
            self.inner
                .bind(py)
                .call_method1("peer", (peer,))
                .map(|x| x.unbind())
        })?;
        let res = into_future(event_loop, coro).await?;
        Python::attach(|py| res.extract(py)).map_err(|e| {
            let cls_name = match Python::attach(|py| self.cls_name(py)) {
                Ok(name) => name,
                Err(e) => return e,
            };
            PyTypeError::new_err(format!("{}.peer(): {}", cls_name, e))
        })
    }

    pub async fn peer_ref(&self, peer: PyPeerId) -> PyResult<Option<PyPeerRef>> {
        Ok(self.peer(peer).await?.map(|info| info.to_ref()))
    }

    pub async fn cache_peer(&self, peer_info: PeerInfo) -> PyResult<()> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            self.inner
                .bind(py)
                .call_method1("cache_peer", (peer_info,))
                .map(|x| x.unbind())
        })?;
        into_future(event_loop, coro).await?;
        Ok(())
    }

    pub async fn updates_state(&self) -> PyResult<PyUpdatesState> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            self.inner
                .bind(py)
                .call_method0("updates_state")
                .map(|x| x.unbind())
        })?;
        let res = into_future(event_loop, coro).await?;
        Python::attach(|py| Ok::<_, PyErr>(res.extract(py)?)).map_err(|e| {
            let cls_name = match Python::attach(|py| self.cls_name(py)) {
                Ok(name) => name,
                Err(e) => return e,
            };
            PyTypeError::new_err(format!("{}.updates_state(): {}", cls_name, e))
        })
    }

    pub async fn set_update_state(&self, update: UpdateStateLike) -> PyResult<()> {
        let event_loop = self.event_loop().await;
        let coro = Python::attach(|py| {
            let update = update.into_pyobject(py)?;
            self.inner
                .bind(py)
                .call_method1("set_update_state", (update,))
                .map(|x| x.unbind())
        })?;
        into_future(event_loop, coro).await?;
        Ok(())
    }
}
