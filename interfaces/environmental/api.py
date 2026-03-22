from core.engine.runner import execute


def run_environment(input_text):
    return execute("eco", {"text": input_text})