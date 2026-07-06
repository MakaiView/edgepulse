from __future__ import annotations

import threading
import time

import lgpio

from edgepulse.drivers.driver import Driver


class GPIODriver(Driver):
    """Raspberry Pi GPIO-backed single indicator driver."""

    def __init__(self, pin: int) -> None:
        self._pin = pin
        self._chip = lgpio.gpiochip_open(0)
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None

        lgpio.gpio_claim_output(self._chip, self._pin, 0)

    def on(self) -> None:
        self._stop_animation()
        lgpio.gpio_write(self._chip, self._pin, 1)

    def off(self) -> None:
        self._stop_animation()
        lgpio.gpio_write(self._chip, self._pin, 0)

    def blink(self, on_time: float, off_time: float) -> None:
        self._start_animation(self._blink_loop, on_time, off_time)

    def breathe(self) -> None:
        # Basic breathe placeholder for v0.0.1-alpha.
        # True PWM fade comes later.
        self.blink(0.75, 0.75)

    def cleanup(self) -> None:
        self._stop_animation()
        lgpio.gpio_write(self._chip, self._pin, 0)
        lgpio.gpiochip_close(self._chip)

    def _start_animation(self, target, *args: float) -> None:
        self._stop_animation()

        self._stop_event.clear()
        self._thread = threading.Thread(
            target=target,
            args=args,
            daemon=True,
        )
        self._thread.start()

    def _stop_animation(self) -> None:
        if self._thread and self._thread.is_alive():
            self._stop_event.set()
            self._thread.join(timeout=1)

        self._thread = None
        self._stop_event.clear()

    def _blink_loop(self, on_time: float, off_time: float) -> None:
        while not self._stop_event.is_set():
            lgpio.gpio_write(self._chip, self._pin, 1)
            time.sleep(on_time)

            if self._stop_event.is_set():
                break

            lgpio.gpio_write(self._chip, self._pin, 0)
            time.sleep(off_time)
