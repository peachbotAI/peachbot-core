from core.shared.conversation import parse_conversation


def run(data):
    parsed = parse_conversation(data["text"])
    tokens = parsed["tokens"]

    state = {
        "entity_type": None,
        "analysis_type": None,
        "signals": []
    }

    # Detection
    if "gene" in tokens:
        state["entity_type"] = "gene"
        state["signals"].append("Gene-level signal detected")

    if "protein" in tokens:
        state["entity_type"] = "protein"
        state["signals"].append("Protein interaction context detected")

    if "gnn" in tokens:
        state["analysis_type"] = "graph-based"
        state["signals"].append("Graph neural network analysis triggered")

    # Alert / insight
    if state["analysis_type"] == "graph-based":
        alert = {
            "level": "INFO",
            "message": "Graph-based biological modeling context identified"
        }
    elif state["entity_type"]:
        alert = {
            "level": "INFO",
            "message": f"{state['entity_type'].capitalize()} level analysis context"
        }
    else:
        alert = {
            "level": "INFO",
            "message": "No significant biological signals detected"
        }

    return {
        "state": state,
        "alert": alert,
        "decision_required": False
    }