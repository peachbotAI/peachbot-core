from core.sbc.engine import SBCState

SBC_ENGINE = SBCState()


def update_state(data):
    SBC_ENGINE.update(data)


def get_state():
    return SBC_ENGINE.get_state()


def get_context():
    return SBC_ENGINE.get_context()