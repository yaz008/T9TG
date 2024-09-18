from replace.load import load_all

MATCHES: dict[str, str] = load_all()

def replace(text: str) -> str:
    for trigger, replace in MATCHES.items():
        text = text.replace(trigger, replace)
    return text