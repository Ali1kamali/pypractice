from typing import Literal
from .practices import easy, medium, hard

def check(
    difficulty: Literal["easy", "medium", "hard"],
    number: int,
    solution
):
    practices = {
        "easy": easy.check,
        "medium": medium.check,
        "hard": hard.check,
    }

    handler = practices.get(difficulty)

    if handler is None:
        raise ValueError(f"Unsupported difficulty: {difficulty}")

    handler(number, solution)
