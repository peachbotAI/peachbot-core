from core.engine.runner import execute

def run_agri(input_text):
    return execute("agri", {"text": input_text})