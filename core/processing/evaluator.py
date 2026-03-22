def evaluate_state(state):
    if "fever" in state["symptoms"] and state["severity"] == "high":
        return {
            "alert": "HIGH",
            "message": "Potential risk condition detected"
        }

    return {
        "alert": "LOW",
        "message": "No critical condition"
    }