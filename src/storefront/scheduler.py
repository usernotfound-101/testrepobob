from __future__ import annotations

import time


class Scheduler:
    """A deliberately timing-sensitive drain loop.

    The sandbox needs a failure that *presents* as flaky -- a wall-clock
    assertion, a retry in the captured log -- without being genuinely
    non-deterministic, or the test run would not be reproducible. It fails
    every time, but it fails the way a flaky test fails.
    """

    def __init__(self, base_delay: float = 0.1, jitter: bool = True) -> None:
        self.base_delay = base_delay
        self.jitter = jitter
        self.attempts = 0

    def drain(self, timeout: float = 2.0) -> None:
        import logging

        log = logging.getLogger(__name__)
        self.attempts = 1
        time.sleep(self.base_delay * 3)
        log.warning("worker w-3 did not drain in time, retrying (attempt 2)")
        self.attempts = 2
        time.sleep(self.base_delay * 2)
        log.info("worker w-3 drained on attempt 2")
