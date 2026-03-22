from core.engine.runner import execute


def run_clinical(input_text):
    return execute("medai", {"text": input_text})