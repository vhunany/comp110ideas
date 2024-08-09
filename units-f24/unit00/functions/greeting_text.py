"""Meet my great friend."""

def announce(name: str) -> str:
    """Present the introduction."""
    return end_with(word=start_with(word=f"my great friend, {name}!", pre="~ Meet "), post=" ~")

def end_with(word: str, post: str) -> str:
    """Add closing."""
    return word + post

def start_with(word: str, pre: str) -> str:
    """Add opening."""
    return pre + word

print(announce(name="Jane Doe"))