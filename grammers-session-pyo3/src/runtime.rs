use std::{
    pin::Pin,
    sync::{Arc, Mutex, OnceLock},
    task::{Context, Poll, Waker},
};

use pyo3::prelude::*;
use pyo3::types::PyCFunction;

static PY_ASYNCIO: OnceLock<Py<PyAny>> = OnceLock::new();
static PY_EVENT_LOOP: OnceLock<Py<PyAny>> = OnceLock::new();

pub fn asyncio(py: Python<'_>) -> PyResult<Py<PyAny>> {
    match PY_ASYNCIO.get() {
        Some(x) => Ok(x.clone_ref(py)),
        None => {
            let asyncio = py.import("asyncio")?.into_any().unbind();
            let copy = asyncio.clone_ref(py);
            PY_ASYNCIO.set(asyncio).unwrap();
            Ok(copy)
        }
    }
}

pub fn event_loop(py: Python<'_>) -> PyResult<Py<PyAny>> {
    match PY_EVENT_LOOP.get() {
        Some(x) => Ok(x.clone_ref(py)),
        None => {
            let asyncio = asyncio(py)?;
            let event_loop = asyncio.call_method0(py, "get_running_loop")?.into_any();
            let copy = event_loop.clone_ref(py);
            PY_EVENT_LOOP.set(event_loop).unwrap();
            Ok(copy)
        }
    }
}

struct Shared {
    result: Option<PyResult<Py<PyAny>>>,
    waker: Option<Waker>,
}

pub struct PyFuture {
    py_coro: Option<Py<PyAny>>,
    concurrent_future: Option<Py<PyAny>>,
    shared: Arc<Mutex<Shared>>,
}

/// 在 Tokio spawn 的任务中安全地 await Python coroutine
pub fn into_future(py_coro: Py<PyAny>) -> PyFuture {
    PyFuture {
        py_coro: Some(py_coro),
        concurrent_future: None,
        shared: Arc::new(Mutex::new(Shared {
            result: None,
            waker: None,
        })),
    }
}

impl std::future::Future for PyFuture {
    type Output = PyResult<Py<PyAny>>;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        // is done
        {
            let mut shared = self.shared.lock().unwrap();

            if let Some(result) = shared.result.take() {
                return Poll::Ready(result);
            }

            shared.waker = Some(cx.waker().clone());
        }

        // first poll to init
        if self.concurrent_future.is_none() {
            let res = Python::attach(|py| {
                let asyncio = py.import("asyncio")?;

                let event_loop = event_loop(py)?;

                let py_coro = self.py_coro.take().unwrap();

                let concurrent_future = asyncio
                    .call_method1("run_coroutine_threadsafe", (py_coro.bind(py), event_loop))?
                    .unbind();

                let shared_cb = self.shared.clone();

                let callback =
                    PyCFunction::new_closure(py, None, None, move |args, _| -> PyResult<()> {
                        let fut = args.get_item(0)?;

                        let result = fut.call_method0("result").map(|x| x.unbind());

                        let mut shared = shared_cb.lock().unwrap();

                        shared.result = Some(result);

                        if let Some(waker) = shared.waker.take() {
                            waker.wake();
                        }

                        Ok(())
                    })?;

                concurrent_future
                    .bind(py)
                    .call_method1("add_done_callback", (callback,))?;

                self.concurrent_future = Some(concurrent_future);

                Ok(py.None())
            });

            if res.is_err() {
                return Poll::Ready(res);
            }
        }

        Poll::Pending
    }
}

impl Drop for PyFuture {
    fn drop(&mut self) {
        if let Some(fut) = &self.concurrent_future {
            Python::attach(|py| {
                let _ = fut.bind(py).call_method0("cancel");
            });
        }
    }
}
