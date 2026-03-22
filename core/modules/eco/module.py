from core.shared.conversation import parse_conversation


def run(data):
    parsed = parse_conversation(data["text"])
    tokens = parsed["tokens"]

    state = {
        "water_quality": "normal",
        "oxygen_level": "normal",
        "pollution": False,
        "alerts": []
    }

    # Logic
    if "pollution" in tokens:
        state["pollution"] = True
        state["water_quality"] = "poor"
        state["alerts"].append("Water pollution detected")

    if "low" in tokens and "oxygen" in tokens:
        state["oxygen_level"] = "low"
        state["alerts"].append("Low dissolved oxygen level")

    # Alert logic
    if state["pollution"] and state["oxygen_level"] == "low":
        alert = {
            "level": "CRITICAL",
            "message": "Severe water degradation detected"
        }
    elif state["pollution"]:
        alert = {
            "level": "WARNING",
            "message": "Pollution detected in water body"
        }
    elif state["oxygen_level"] == "low":
        alert = {
            "level": "WARNING",
            "message": "Low oxygen level detected"
        }
    else:
        alert = {
            "level": "INFO",
            "message": "Environment within normal parameters"
        }

    return {
        "state": state,
        "alert": alert,
        "decision_required": False
    }