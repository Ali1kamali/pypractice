
from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            ((1, 2), 3),
            ((5, 5), 10),
            ((-1, 1), 0),
            ((10, 20), 30),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(f"{self.BLUE}{self.BOLD}=== Exercise 1: Sum Two Numbers ==={self.RESET}")
        print("Write a function that receives two numbers and returns their sum.\n")

    def help(self):
        """توضیحات تکمیلی و یک نمونه از جواب درست"""

        print(f"💡 {self.yellow("Hint:")} You can use the '+' operator.")
        print(f"💡 {self.yellow("Example Solution:")}")
        print(f"   def solution(a, b):")
        print(f"       return a + b")

    def show_tests(self):
        """نمایش تست‌هایی که قرار است اجرا شوند"""

        print("--- Upcoming Tests ---")

        for i, (inputs, expected) in enumerate(self.tests, 1):
            input_str = ", ".join(map(str, inputs))
            print(f"Test {i}: Input({input_str}) -> Expected: {expected}")
        print("----------------------")

    def check(self, solution):
        self._check_function(solution)
