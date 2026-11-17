from typing import Literal
from .practices import easy, medium, hard


def help(
    difficulty: Literal["easy", "medium", "hard"],
    number: int
):
    practices = {
        "easy": easy.help,
        "medium": medium.help,
        "hard": hard.help,
    }

    handler = practices.get(difficulty)

    if handler is None:
        raise ValueError(f"Unsupported difficulty: {difficulty}")

    return handler(number)
