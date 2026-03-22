def evaluate(state, context=None):
    severity = state.get("severity", {}).get("value", "low")
    weight = state.get("severity", {}).get("effective_weight", 0)

    priority = 0
    relations = 0

    if context:
        priority = context.get("priority_score", 0)
        relations = context.get("relation_count", 0)

    # 🔥 PRIORITY-DRIVEN DECISION

    if priority > 2.5:
        return {
            "level": "CRITICAL",
            "message": "System-wide critical condition detected"
        }

    if severity == "high" and weight > 0.6:
        return {
            "level": "CRITICAL",
            "message": "High severity condition"
        }

    if severity == "high" or relations >= 2:
        return {
            "level": "WARNING",
            "message": "Elevated multi-factor condition"
        }

    return {
        "level": "INFO",
        "message": "No critical condition"
    }