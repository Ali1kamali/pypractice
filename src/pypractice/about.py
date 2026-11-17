from typing import Literal
from .practices import easy, medium, hard

def about(
    difficulty: Literal["easy", "medium", "hard"],
    number: int
):
    practices = {
        "easy": easy.about,
        "medium": medium.about,
        "hard": hard.about,
    }

    handler = practices.get(difficulty)

    if handler is None:
        raise ValueError(f"Unsupported difficulty: {difficulty}")

    return handler(number)
