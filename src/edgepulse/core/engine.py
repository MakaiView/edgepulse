from __future__ import annotations

from edgepulse.core.status import Status, StatusLevel


class StatusEngine:
    """Maintains the overall health of the system."""

    def __init__(self) -> None:
        self._statuses: dict[str, Status] = {}

    def update(self, status: Status) -> None:
        """Update the latest status from a source."""
        self._statuses[status.source] = status

    @property
    def current_status(self) -> Status:
        """Return the highest priority status currently active."""

        if not self._statuses:
            return Status(
                level=StatusLevel.BOOTING,
                message="No health checks have reported yet.",
                source="engine",
            )

        return max(
            self._statuses.values(),
            key=lambda status: status.level,
        )

    @property
    def all_statuses(self) -> dict[str, Status]:
        """Return a copy of all current statuses."""
        return self._statuses.copy()
