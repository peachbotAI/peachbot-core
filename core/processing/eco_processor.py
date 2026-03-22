def process_eco(parsed):
    tokens = parsed["tokens"]

    alerts = []

    if "pollution" in tokens:
        alerts.append("Water pollution detected")

    if "low" in tokens and "oxygen" in tokens:
        alerts.append("Low dissolved oxygen level")

    return {
        "domain": "eco",
        "alerts": alerts
    }