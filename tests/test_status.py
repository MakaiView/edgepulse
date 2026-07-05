from edgepulse.core.status import Status, StatusLevel


def test_status_serializes_to_dict() -> None:
    status = Status(
        level=StatusLevel.HEALTHY,
        message="System operating normally.",
        source="test",
        details={"check": "ok"},
    )

    data = status.to_dict()

    assert data["level"] == "HEALTHY"
    assert data["level_value"] == 30
    assert data["message"] == "System operating normally."
    assert data["source"] == "test"
    assert data["details"] == {"check": "ok"}
    assert data["is_problem"] is False
    assert "timestamp" in data


def test_warning_is_problem() -> None:
    status = Status(
        level=StatusLevel.WARNING,
        message="Something needs attention.",
    )

    assert status.is_problem is True
