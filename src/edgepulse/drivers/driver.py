from __future__ import annotations

from abc import ABC, abstractmethod


class Driver(ABC):
    """Base class for all EdgePulse device drivers."""

    @abstractmethod
    def on(self) -> None:
        """Turn the indicator on."""
        ...

    @abstractmethod
    def off(self) -> None:
        """Turn the indicator off."""
        ...

    @abstractmethod
    def blink(
        self,
        on_time: float,
        off_time: float,
    ) -> None:
        """Blink the indicator."""
        ...

    @abstractmethod
    def breathe(self) -> None:
        """Run the breathing animation."""
        ...

    @abstractmethod
    def cleanup(self) -> None:
        """Release any hardware resources."""
        ...
