from core.shared.conversation import parse_conversation


def run(data):
    parsed = parse_conversation(data["text"])
    tokens = parsed["tokens"]

    state = {
        "soil_moisture": "normal",
        "pest_risk": False,
        "crop_health": "stable",
        "alerts": []
    }

    # Logic
    if "dry" in tokens:
        state["soil_moisture"] = "low"
        state["alerts"].append("Soil moisture low")

    if "pest" in tokens:
        state["pest_risk"] = True
        state["alerts"].append("Pest risk detected")

    # Alert logic
    if state["soil_moisture"] == "low" and state["pest_risk"]:
        alert = {
            "level": "CRITICAL",
            "message": "Crop stress condition detected"
        }
    elif state["soil_moisture"] == "low":
        alert = {
            "level": "WARNING",
            "message": "Irrigation required"
        }
    elif state["pest_risk"]:
        alert = {
            "level": "WARNING",
            "message": "Pest activity detected"
        }
    else:
        alert = {
            "level": "INFO",
            "message": "Crop conditions stable"
        }

    return {
        "state": state,
        "alert": alert,
        "decision_required": False
    }