import importlib


def about(number: int):
    try:
        module = importlib.import_module(f".e{number}", package=__package__)
        c = module.Exercise()
        c.about()

    except ModuleNotFoundError:
        raise ImportError(f"Exercise e{number} not found")


def check(number: int, solution):
    try:
        module = importlib.import_module(f".e{number}", package=__package__)
        c = module.Exercise()
        c.check(solution)

    except ModuleNotFoundError:
        raise ImportError(f"Exercise e{number} not found")


def show_tests(number: int):
    try:
        module = importlib.import_module(f".e{number}", package=__package__)
        c = module.Exercise()
        c.show_tests()

    except ModuleNotFoundError:
        raise ImportError(f"Exercise e{number} not found")


def help(number: int):
    try:
        module = importlib.import_module(f".e{number}", package=__package__)
        c = module.Exercise()
        if hasattr(c, "help"):
            print(c.help())
        else:
            print(f"No help text available for {number}")

    except ModuleNotFoundError:
        raise ImportError(f"Exercise e{number} not found")
