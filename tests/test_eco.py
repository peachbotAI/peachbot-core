from core.engine.runner import execute


def test_eco():
    result = execute("eco", {"text": "water pollution"})

    assert "state" in result