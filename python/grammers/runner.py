import signal
import threading
import functools
import contextvars
import asyncio

class Runner(asyncio.Runner):
    def run_forever(self, *, context=None):
        """Run forever in the embedded event loop, until loo.stop() called.
        
        Args:
            setup: 可选的协程/协程函数，在 run_forever 之前执行（用于启动后台任务）
            context: 可选的上下文
        """
        if events._get_running_loop() is not None:
            raise RuntimeError(
                "run_forever() cannot be called from a running event loop")
        
        self._lazy_init()
        
        if context is None:
            context = self._context
        
        if (threading.current_thread() is threading.main_thread()
            and signal.getsignal(signal.SIGINT) is signal.default_int_handler
        ):
            sigint_handler = self._on_sigint
            try:
                signal.signal(signal.SIGINT, sigint_handler)
            except ValueError:
                sigint_handler = None
        
        self._interrupt_count = 0
        
        try:
            self._loop.run_forever()
        finally:
            # 恢复信号处理器
            if sigint_handler is not None:
                if signal.getsignal(signal.SIGINT) is sigint_handler:
                    signal.signal(signal.SIGINT, signal.default_int_handler)

    def _on_sigint(self, signum, frame):
        self._interrupt_count += 1
        if self._interrupt_count == 1:
            # wakeup loop if it is blocked by select() with long timeout
            self._loop.call_soon_threadsafe(lambda: None)
            return
        raise KeyboardInterrupt()


def run_forever(*, debug=None, loop_factory=None, setup=None):
    """Run the event loop until loop.stop() is called.

    This function runs forever, taking care of
    managing the asyncio event loop, finalizing asynchronous
    generators and closing the default executor.

    This function cannot be called when another asyncio event loop is
    running in the same thread.

    This function always creates a new event loop and closes it at the end.
    It should be used as a main entry point for asyncio programs, and should
    ideally only be called once.

    The executor is given a timeout duration of 5 minutes to shutdown.
    If the executor hasn't finished within that duration, a warning is
    emitted and the executor is closed.

    Args:
        debug: If debug is True, the event loop will be run in debug mode.
        loop_factory: If loop_factory is passed, it is used for new event loop creation.

    Example:
        async def background_task():
            while True:
                print("working...")
                await asyncio.sleep(1)
        
        asyncio.create_task(background_task())
        run_forever()
    """
    if events._get_running_loop() is not None:
        raise RuntimeError(
            "run_forever() cannot be called from a running event loop")
    
    with RunnerForever(debug=debug, loop_factory=loop_factory) as runner:
        return runner.run_forever()