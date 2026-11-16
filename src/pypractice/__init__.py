from typing import Literal

from .practices.easy import about as easy_about
from .practices.medium import about as medium_about
from .practices.hard import about as hard_about

from .practices.easy import check as easy_check
from .practices.medium import check as medium_check
from .practices.hard import check as hard_check


def about(
    difficulty: Literal["easy", "medium", "hard"],
    number: int
):
    practices = {
        "easy": easy_about,
        "medium": medium_about,
        "hard": hard_about,
    }

    handler = practices.get(difficulty)

    if handler is None:
        raise ValueError(f"Unsupported difficulty: {difficulty}")

    return handler(number)


def check(
    difficulty: Literal["easy", "medium", "hard"],
    number: int,
    solution
):
    practices = {
        "easy": easy_check,
        "medium": medium_check,
        "hard": hard_check,
    }

    handler = practices.get(difficulty)

    if handler is None:
        raise ValueError(f"Unsupported difficulty: {difficulty}")

    handler(number , solution)
