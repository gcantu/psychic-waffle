from .utils import transliterate, add_digits


def get_destiny_number(name: str) -> int:
    total = 0
    name = name.replace(' ', '').upper()

    for i in name:
        total += transliterate(i)

    dest_num = add_digits(total)

    return dest_num
