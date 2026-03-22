import json
from datetime import datetime

LOG_FILE = "audit_log.json"


def log_event(event):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)