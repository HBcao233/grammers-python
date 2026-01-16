use super::PyClient;
use pyo3::prelude::*;
// use pyo3_async_runtimes::tokio::get_runtime;

#[cfg(feature = "stub-gen")]
use pyo3_stub_gen::derive::*;


#[cfg_attr(feature = "stub-gen", gen_stub_pymethods)]
#[pymethods]
impl PyClient {
  #[pyo3(signature = ())]
  async fn start(&self) -> PyResult<()> {
    // let inner = self.inner.clone();
    println!("start");
    self.authorize().await?;
    Ok(())
  }
  
  /*
  #[pyo3(signature = ())]
  async fn idle(&self) -> PyResult<()> {
    // let inner = self.inner.clone();
    
    #[cfg(unix)]
    {
      use tokio::signal::unix::{signal, SignalKind};
      
      let mut sigint = signal(SignalKind::interrupt()).map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
      let mut sigterm = signal(SignalKind::terminate()).map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
      let mut sigquit = signal(SignalKind::quit()).map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
      println!("a");
      tokio::select! {
        _ = sigint.recv() => "SIGINT",
        _ = sigterm.recv() => "SIGTERM",
        _ = sigquit.recv() => "SIGQUIT",
      };
      println!("b");
    }
    
    #[cfg(windows)]
    {
      use tokio::signal::windows;
      
      let mut ctrl_c = windows::ctrl_c().map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
      let mut ctrl_break = windows::ctrl_break().map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
      let mut ctrl_close = windows::ctrl_close().map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
      let mut ctrl_shutdown = windows::ctrl_shutdown().map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
      
      tokio::select! {
        _ = ctrl_c.recv() => println!("Received Ctrl+C"),
        _ = ctrl_break.recv() => println!("Received Ctrl+Break"),
      };
    }
    
    Ok(())
  }*/
  
  #[pyo3(signature = ())]
  async fn stop(&mut self) -> PyResult<()> {
    println!("stop");
    let pool_task = self.pool_task.take();
    self.updates.sync_update_state();
    self.handle.quit();
    if let Some(task) = pool_task {
      let _ = task.await;
    }
    Ok(())
  }
  
  /*
  #[pyo3(signature = (coroutine=None))]
  fn run<'py>(&self, py: Python<'py>, coroutine: Option<&Bound<'py, PyAny>>) -> PyResult<()> {
    // let inner = self.inner.clone();
    
    let asyncio = py.import("asyncio")?;
    let running_loop: PyResult<Bound<'_, PyAny>> = asyncio.call_method0("get_running_loop");
    if running_loop.is_ok() {
      return Err(PyErr::new::<PyRuntimeError, _>(
        "You must call client.run() outside of an asyncio event loop. Otherwise, you can use client.start(), client.idle(), and client.stop() metheds."
      ));
    }
    
    // let event_loop = asyncio.call_method0("new_event_loop")?;
    // asyncio.call_method1("set_event_loop", (&event_loop,))?;
    
    println!("a");
    get_runtime().block_on(async {
      Python::attach(|py| {
        let binging = self._run(py)?;
        let coro = coroutine.unwrap_or(&binging);
        into_future(coro)
      })?.await
    })?;
    println!("b");
    
    let _result = asyncio.call_method1("run", (coro,))?;
    
    // event_loop.call_method0("close")?;
    Ok(())
  }*/
}
