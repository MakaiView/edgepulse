from edgepulse.config.config import Config


def test_configuration_loads() -> None:
    config = Config()

    assert config.driver == "mock"
    assert config.gpio_pin == 18
    assert config.startup_delay == 5
    assert config.status_duration == 2
