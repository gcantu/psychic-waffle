from .constants import CHAR_INDEX


def add_digits(num: int) -> int:
    return (num - 1) % 9 + 1 if num > 0 else 0


def transliterate(val, char_index=CHAR_INDEX):
    """convert each letter character in your Name to a number using the transliteration character index"""

    return char_index.find(val) % 10
