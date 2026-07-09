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
                from edgepulse.drivers.gpio import GPIODriver

                return GPIODriver(pin=config.gpio_pin)

            case _:
                raise ValueError(f"Unknown driver type '{config.driver}'")
