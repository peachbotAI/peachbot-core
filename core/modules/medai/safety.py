def evaluate(state):
    symptoms = state["symptoms"]
    severity = state["severity"]

    if "fever" in symptoms and severity == "high":
        return {
            "level": "CRITICAL",
            "message": "High fever detected. Immediate attention required."
        }

    if "fever" in symptoms:
        return {
            "level": "WARNING",
            "message": "Fever present. Monitor condition."
        }

    return {
        "level": "INFO",
        "message": "No critical symptoms detected."
    }