
from multiprocessing import context

from core import state
from core.shared.conversation import parse_conversation
from core.modules.medai.extractor import extract_clinical_info
from core.modules.medai.state import update_state, get_state
from core.modules.medai.safety import evaluate
from core.modules.medai.state import get_context


def run(data):
    parsed = parse_conversation(data["text"])
    clinical = extract_clinical_info(parsed)

    update_state(clinical)
    state = get_state()

    context = get_context()
    alert = evaluate(state, context)
    return {
        "state": state,
        "context": context,
        "alert": alert,
        "decision_required": True
    }