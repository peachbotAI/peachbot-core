def parse_conversation(text):
    return {
        "raw_text": text,
        "tokens": text.lower().split()
    }