from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import IntEnum
from typing import Any


class StatusLevel(IntEnum):
    """Ordered health/status levels for EdgePulse."""

    OFF = 0
    BOOTING = 10
    STARTING = 20
    HEALTHY = 30
    INFO = 40
    UPDATING = 50
    WARNING = 60
    CRITICAL = 70
    SHUTTING_DOWN = 80


@dataclass(frozen=True, slots=True)
class Status:
    """A normalized status report from EdgePulse core or a plugin."""

    level: StatusLevel
    message: str
    source: str = "system"
    details: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    @property
    def is_problem(self) -> bool:
        """Return True when this status should be treated as degraded."""
        return self.level >= StatusLevel.WARNING

    def to_dict(self) -> dict[str, Any]:
        """Serialize this status for CLI, API, MQTT, or logs."""
        return {
            "level": self.level.name,
            "level_value": int(self.level),
            "message": self.message,
            "source": self.source,
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
            "is_problem": self.is_problem,
        }
