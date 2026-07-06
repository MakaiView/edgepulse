from __future__ import annotations

from pathlib import Path

import yaml


class Config:
    """EdgePulse configuration."""

    def __init__(self, filename: str = "config/config.yaml") -> None:
        self.path = Path(filename)

        with self.path.open("r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)

    @property
    def driver(self) -> str:
        return self.data["driver"]["type"]

    @property
    def gpio_pin(self) -> int:
        return self.data["gpio"]["pin"]

    @property
    def startup_delay(self) -> int:
        return self.data["demo"]["startup_delay"]

    @property
    def status_duration(self) -> int:
        return self.data["demo"]["status_duration"]
