import importlib


def about(number: int):
    try:
        module = importlib.import_module(f".e{number}", package=__package__)
    except ModuleNotFoundError:
        raise ImportError(f"Exercise e{number} not found")

    module.about()


def check(number: int , solution):
    try:
        module = importlib.import_module(f".e{number}", package=__package__)
    except ModuleNotFoundError:
        raise ImportError(f"Exercise e{number} not found")

    module.check(solution)