from __future__ import annotations

from edgepulse.drivers.driver import Driver


class MockDriver(Driver):
    """Mock driver used during development."""

    def on(self) -> None:
        print("💡 ON")

    def off(self) -> None:
        print("💡 OFF")

    def blink(
        self,
        on_time: float,
        off_time: float,
    ) -> None:
        print(f"💡 BLINK ({on_time:.2f}s / {off_time:.2f}s)")

    def breathe(self) -> None:
        print("💡 BREATHE")

    def cleanup(self) -> None:
        print("💡 CLEANUP")
