use std::{
    pin::Pin,
    sync::{Arc, Mutex},
    task::{Context, Poll, Waker},
};

use pyo3::prelude::*;
use pyo3::types::PyCFunction;
use pyo3::sync::PyOnceLock;

static ASYNCIO: PyOnceLock<Py<PyModule>> = PyOnceLock::new();
static EVENT_LOOP: PyOnceLock<Py<PyAny>> = PyOnceLock::new();

pub fn asyncio<'py>(py: Python<'py>) -> PyResult<&'py Bound<'py, PyModule>> {
    ASYNCIO
        .get_or_try_init(py, || Ok(py.import("asyncio")?.unbind()))
        .map(|asyncio| asyncio.bind(py))
}

pub fn event_loop<'py>(py: Python<'py>) -> PyResult<&'py Bound<'py, PyAny>> {
    EVENT_LOOP
        .get_or_try_init(py, || -> PyResult<Py<PyAny>> {
            let asyncio = asyncio(py)?;

            Ok(asyncio
                .call_method0(pyo3::intern!(py, "get_running_loop"))?
                .unbind())
        })
        .map(|x| x.bind(py))
}

struct PyFutureInner {
    py_coro: Option<Py<PyAny>>,
    concurrent_future: Option<Py<PyAny>>,
    result: Option<PyResult<Py<PyAny>>>,
    waker: Option<Waker>,
}

#[derive(Clone)]
pub struct PyFuture {
    inner: Arc<Mutex<PyFutureInner>>,
}

/// 在 Tokio spawn 的任务中安全地 await Python coroutine
pub fn into_future(py_coro: Py<PyAny>) -> PyFuture {
    PyFuture {
        inner: Arc::new(Mutex::new(PyFutureInner {
            py_coro: Some(py_coro),
            concurrent_future: None,
            result: None,
            waker: None,
        })),
    }
}

impl std::future::Future for PyFuture {
    type Output = PyResult<Py<PyAny>>;

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        let (result, py_coro) = {
            let inner = self.inner.clone();
            let mut guard = inner.lock().unwrap();
            guard.waker = Some(cx.waker().clone());
            (guard.result.take(), guard.py_coro.take())
        };
        // is done
        if let Some(res) = result {
            return Poll::Ready(res);
        }

        // first poll to init
        if let Some(coro) = py_coro {
            let inner = self.inner.clone();
            let res = Python::attach(|py| {
                let asyncio = asyncio(py)?;
                let event_loop = event_loop(py)?;

                let concurrent_future =
                    asyncio.call_method1("run_coroutine_threadsafe", (coro, event_loop))?;

                let callback =
                    PyCFunction::new_closure(py, None, None, move |args, _| -> PyResult<()> {
                        let fut = args.get_item(0)?;
                        let result = fut.call_method0("result").map(|x| x.unbind());

                        let waker = {
                            let mut guard = inner.lock().unwrap();
                            guard.result = Some(result);
                            guard.waker.take()
                        };

                        if let Some(waker) = waker {
                            waker.wake();
                        }

                        Ok(())
                    })?;

                concurrent_future.call_method1("add_done_callback", (callback,))?;

                Ok(concurrent_future.unbind())
            });

            match res {
                Ok(concurrent_future) => {
                    self.inner.lock().unwrap().concurrent_future = Some(concurrent_future);
                }
                Err(e) => return Poll::Ready(Err(e)),
            }
        }

        Poll::Pending
    }
}

/*
impl Drop for PyFuture {
    fn drop(&mut self) {
        let concurrent_future = {
            let inner = self.inner.clone();
            let guard = inner.lock().unwrap();
            match &guard.concurrent_future {
                None => None,
                Some(x) => Some(Python::attach(|py| x.clone_ref(py))),
            }
        };
        if let Some(fut) = &concurrent_future {
            Python::attach(|py| {
                let event_loop = event_loop(py).unwrap();
                let cancel_func = fut.bind(py).getattr("cancel").unwrap();
                let _ = event_loop.call_method1("call_soon_threadsafe", (cancel_func,));
            });
        }
    }
}*/
