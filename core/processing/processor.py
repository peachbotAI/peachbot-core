def process_input(data):
    text = data["text"]

    # placeholder
    extracted = {
        "symptom": "fever" if "fever" in text.lower() else None,
        "severity": "high" if "high" in text.lower() else "low"
    }

    return extracted