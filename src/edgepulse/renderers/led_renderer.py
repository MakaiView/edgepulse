from __future__ import annotations

from edgepulse.core.status import Status, StatusLevel
from edgepulse.drivers.driver import Driver


class SingleLEDRenderer:
    """Render EdgePulse status using a single indicator."""

    def __init__(self, driver: Driver) -> None:
        self._driver = driver

    def render(self, status: Status) -> None:

        match status.level:

            case StatusLevel.OFF:
                self._driver.off()

            case StatusLevel.BOOTING:
                self._driver.breathe()

            case StatusLevel.STARTING:
                self._driver.blink(0.5, 0.5)

            case StatusLevel.HEALTHY:
                self._driver.on()

            case StatusLevel.WARNING:
                self._driver.blink(0.25, 0.25)

            case StatusLevel.CRITICAL:
                self._driver.blink(0.10, 0.10)

            case StatusLevel.SHUTTING_DOWN:
                self._driver.breathe()

            case _:
                self._driver.on()
