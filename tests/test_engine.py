from edgepulse.core.engine import StatusEngine
from edgepulse.core.status import Status, StatusLevel


def test_empty_engine_reports_booting() -> None:
    engine = StatusEngine()

    assert engine.current_status.level == StatusLevel.BOOTING


def test_highest_priority_status_wins() -> None:
    engine = StatusEngine()

    engine.update(
        Status(
            level=StatusLevel.HEALTHY,
            message="System healthy",
            source="system",
        )
    )

    engine.update(
        Status(
            level=StatusLevel.WARNING,
            message="DNS latency",
            source="adguard",
        )
    )

    assert engine.current_status.level == StatusLevel.WARNING


def test_critical_overrides_warning() -> None:
    engine = StatusEngine()

    engine.update(
        Status(
            level=StatusLevel.WARNING,
            message="DNS latency",
            source="adguard",
        )
    )

    engine.update(
        Status(
            level=StatusLevel.CRITICAL,
            message="VPN disconnected",
            source="tailscale",
        )
    )

    assert engine.current_status.level == StatusLevel.CRITICAL


def test_engine_tracks_multiple_sources() -> None:
    engine = StatusEngine()

    engine.update(
        Status(
            level=StatusLevel.HEALTHY,
            message="Healthy",
            source="system",
        )
    )

    engine.update(
        Status(
            level=StatusLevel.INFO,
            message="Checking updates",
            source="updater",
        )
    )

    assert len(engine.all_statuses) == 2
