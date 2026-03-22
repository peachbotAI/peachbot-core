from core.engine.runner import execute


def test_agri_dry_soil():
    result = execute("agri", {"text": "dry soil condition"})

    assert result["state"]["soil_moisture"] == "low"
    assert result["alert"]["level"] == "WARNING"


def test_agri_pest_risk():
    result = execute("agri", {"text": "pest detected in crops"})

    assert result["state"]["pest_risk"] is True
    assert result["alert"]["level"] == "WARNING"


def test_agri_critical_condition():
    result = execute("agri", {"text": "dry soil and pest attack"})

    assert result["alert"]["level"] == "CRITICAL"


def test_agri_normal():
    result = execute("agri", {"text": "healthy crops"})

    assert result["alert"]["level"] == "INFO"