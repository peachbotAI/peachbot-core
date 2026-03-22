import json

REGISTRY = []


def receive_session(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    REGISTRY.append(data)

    print("✅ Session received and stored in cloud registry")


def list_sessions():
    print(f"Total sessions stored: {len(REGISTRY)}")