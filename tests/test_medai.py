from core.engine.runner import execute


def test_medai_basic():
    result = execute("medai", {"text": "fever"})

    assert "state" in result
    assert "alert" in result