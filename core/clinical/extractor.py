def extract_clinical_info(parsed):
    tokens = parsed["tokens"]

    symptoms = []
    severity = "low"

    if "fever" in tokens:
        symptoms.append("fever")

    if "cough" in tokens:
        symptoms.append("cough")

    if "pain" in tokens:
        symptoms.append("pain")

    if "severe" in tokens or "high" in tokens:
        severity = "high"

    return {
        "symptoms": symptoms,
        "severity": severity
    }