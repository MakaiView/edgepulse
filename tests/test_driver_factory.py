import pytest

from edgepulse.config.config import Config
from edgepulse.drivers.factory import DriverFactory
from edgepulse.drivers.mock import MockDriver


def test_driver_factory_creates_mock_driver() -> None:
    config = Config("config/config.yaml")

    driver = DriverFactory.create(config)

    assert isinstance(driver, MockDriver)


def test_driver_factory_rejects_unknown_driver() -> None:
    config = Config("config/config.yaml")
    config.data["driver"]["type"] = "missing"

    with pytest.raises(ValueError, match="Unknown driver type"):
        DriverFactory.create(config)
