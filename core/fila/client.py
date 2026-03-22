from core.shared.output.manager import get_path
import json


def export_session(session_data):
    filename = f"fila_{session_data['id']}.json"
    path = get_path("fila_exports", filename)

    with open(path, "w") as f:
        json.dump(session_data, f, indent=2)

    print(f"📤 FILA Exported: {path}")

    return path