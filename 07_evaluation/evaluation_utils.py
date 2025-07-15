from difflib import SequenceMatcher

def similarity(a: str, b: str) -> float:
    return round(SequenceMatcher(None, a.lower(), b.lower()).ratio(), 2)
