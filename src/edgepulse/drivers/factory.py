from __future__ import annotations

from edgepulse.config.config import Config
from edgepulse.drivers.driver import Driver
from edgepulse.drivers.mock import MockDriver


class DriverFactory:
    """Instantiate the configured EdgePulse driver."""

    @staticmethod
    def create(config: Config) -> Driver:
        match config.driver:

            case "mock":
                return MockDriver()

            case "gpio":
                raise NotImplementedError("GPIO driver has not been implemented yet.")

            case _:
                raise ValueError(f"Unknown driver type '{config.driver}'")
