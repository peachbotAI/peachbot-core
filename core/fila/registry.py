REGISTRY = {
    "sessions": [],
    "models": []
}


def register_session(session):
    REGISTRY["sessions"].append(session)


def list_sessions():
    return len(REGISTRY["sessions"])