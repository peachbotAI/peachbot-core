STATE = {}


def update_state(key, value):
    STATE[key] = value


def get_state():
    return STATE