from core.shared.output.manager import init_output_dirs, get_path
from core.fila.client import export_session
import json
from datetime import datetime

SESSION = {
    "id": None,
    "start_time": None,
    "records": []
}


def start_session():
    init_output_dirs()

    SESSION["id"] = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    SESSION["start_time"] = datetime.utcnow().isoformat()
    SESSION["records"] = []

    print(f"\n Session Started: {SESSION['id']}\n")


def add_record(input_text, state, alert, decision):
    SESSION["records"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "input": input_text,
        "state": state,
        "alert": alert,
        "decision": decision
    })


def save_session():
    filename = f"session_{SESSION['id']}.json"
    path = get_path("sessions", filename)

    with open(path, "w") as f:
        json.dump(SESSION, f, indent=2)

    print(f"\n Session saved to {path}")

    # FILA export
    export_session(SESSION)