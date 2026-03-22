import json

AGGREGATED_DATA = []


def receive_export(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    AGGREGATED_DATA.append(data)

    print("FILA Aggregation Complete")


def get_aggregated_count():
    return len(AGGREGATED_DATA)