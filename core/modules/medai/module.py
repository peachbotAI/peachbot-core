from multiprocessing import context

from core import state
from core.shared.conversation import parse_conversation
from core.modules.medai.extractor import extract_clinical_info
from core.modules.medai.state import update_state, get_state
from core.modules.medai.safety import evaluate
from core.modules.medai.state import get_context

# Knowledge Layer
from core.knowledge import enrich_with_knowledge
from core.knowledge import adaptive_learn

def build_signal_attribution(update_payload):
    """
    Explain which signals influenced the decision
    """

    attribution = []

    for key, value in update_payload.items():

        # Skip raw fields
        if key in ["symptoms", "severity"]:
            continue

        # Knowledge signals
        if key.startswith("knowledge_"):
            attribution.append({
                "type": "knowledge",
                "source": key.replace("knowledge_", ""),
                "weight": value.get("weight", 0)
            })

    # Add base clinical signals
    symptoms = update_payload.get("symptoms", [])
    for symptom in symptoms:
        attribution.append({
            "type": "clinical",
            "source": symptom,
            "weight": 1  # base weight
        })

    severity = update_payload.get("severity")
    if severity:
        attribution.append({
            "type": "clinical",
            "source": f"severity_{severity}",
            "weight": 1
        })

    return attribution

def compute_confidence(context):
    """
    Confidence based on SBC priority score (from context)
    """

    priority = context.get("priority_score", 0)

    try:
        priority = float(priority)
    except:
        priority = 0

    # Normalize (tunable)
    confidence = min(priority / 5.0, 1.0)

    return round(confidence, 2)


def run(data):
    # 1️ Parse input
    parsed = parse_conversation(data["text"])

    # 2️ Extract structured clinical signal
    clinical = extract_clinical_info(parsed)

    # 3️ Knowledge enrichment
    clinical = enrich_with_knowledge(clinical, domain="medai")

    # 4️ Convert knowledge → SBC-compatible signals
    knowledge = clinical.pop("knowledge", {})

    update_payload = dict(clinical)

    if knowledge:
        tags = knowledge.get("knowledge_tags", [])
        weight = knowledge.get("knowledge_weight", 0)

        for tag in tags:
            boosted_weight = weight * 2.0 # Tunable boost factor
            update_payload[f"knowledge_{tag}"] = {
                "value": "present",
                "weight": boosted_weight
            }

    # 5️ Update SBC state
    update_state(update_payload)

    # 6️ Retrieve state + context
    state_data = get_state()
    context = get_context()
    
    # Adaptive learning 
    adaptive_learn(update_payload)
    

    # 7️ Safety evaluation
    alert = evaluate(state_data, context)

    attribution = build_signal_attribution(update_payload)
    confidence = compute_confidence(context)

    # 8️ Output
    return {
        "state": state_data,
        "context": context,
        "alert": alert,
        "confidence": confidence,
        "attribution": attribution,
        "decision_required": True
    }