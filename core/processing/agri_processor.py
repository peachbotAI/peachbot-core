def process_agri(parsed):
    tokens = parsed["tokens"]

    alerts = []

    if "dry" in tokens:
        alerts.append("Soil moisture low")

    if "pest" in tokens:
        alerts.append("Pest risk detected")

    return {
        "domain": "agri",
        "alerts": alerts
    }