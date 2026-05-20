"""String utility functions — implement the TODOs using Devin."""


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Rules:
        - Lowercase all characters.
        - Replace spaces with hyphens.
        - Remove any character that is not alphanumeric or a hyphen.
        - Collapse consecutive hyphens into a single hyphen.
        - Strip leading and trailing hyphens.

    Args:
        text: The input string.

    Returns:
        A URL-friendly slug string.
    """
    import re
    import unicodedata
    text = unicodedata.normalize("NFC", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = text.replace(" ", "-")
    text = re.sub(r"[^a-z0-9-]", "", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    return text


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to a maximum length, appending a suffix if truncated.

    Rules:
        - If text length <= max_length, return it unchanged.
        - Otherwise, trim to (max_length - len(suffix)) characters and append the suffix.
        - max_length must be >= len(suffix); raise ValueError if not.

    Args:
        text: The input string.
        max_length: Maximum allowed length of the result (including suffix).
        suffix: String to append when truncating.

    Returns:
        The original or truncated string.

    Raises:
        ValueError: If max_length is less than the length of the suffix.
    """
    if max_length < len(suffix):
        raise ValueError("max_length must be >= len(suffix)")
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def count_words(text: str) -> int:
    """Count the number of words in text.

    A 'word' is any contiguous sequence of non-whitespace characters.
    Leading/trailing whitespace and multiple spaces between words are handled.

    Args:
        text: The input string.

    Returns:
        The number of words.
    """
    return len(text.split()) if text.strip() else 0
