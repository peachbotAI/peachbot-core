STATE = {
    "symptoms": [],
    "severity": "low",
    "history": []
}


def update_state(data):
    for s in data["symptoms"]:
        if s not in STATE["symptoms"]:
            STATE["symptoms"].append(s)

    STATE["severity"] = data["severity"]
    STATE["history"].append(data)


def get_state():
    return STATE