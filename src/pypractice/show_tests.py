from typing import Literal
from .practices import easy, medium, hard

def show_tests(
    difficulty: Literal["easy", "medium", "hard"],
    number: int
):
    practices = {
        "easy": easy.show_tests,
        "medium": medium.show_tests,
        "hard": hard.show_tests,
    }

    handler = practices.get(difficulty)

    if handler is None:
        raise ValueError(f"Unsupported difficulty: {difficulty}")

    return handler(number)
