STATE = {
    "symptoms": [],
    "severity": None
}


def update_state(data):
    if data["symptom"]:
        STATE["symptoms"].append(data["symptom"])

    STATE["severity"] = data["severity"]


def get_state():
    return STATE