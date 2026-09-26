import time

from storefront import Scheduler


def test_retry_backoff():
    scheduler = Scheduler(base_delay=0.1, jitter=True)
    started = time.monotonic()
    scheduler.drain(timeout=2.0)
    assert time.monotonic() - started < 0.4
