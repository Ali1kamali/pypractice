from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            ((2, 3), 6),
            ((5, 5), 25),
            ((1, 7), 7),
            ((0, 100), 0),
            ((-2, 3), -6),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(
            f"{self.BLUE}{self.BOLD}=== Exercise 3: Multiply Two Numbers ==={self.RESET}")
        print("Write a function that receives two numbers and returns their product.\n")

    def help(self):
        """توضیحات تکمیلی و یک نمونه از جواب درست"""

        print(f"💡 {self.yellow("Hint:")} You can use the '*' operator.")
        print(f"💡 {self.yellow("Example Solution:")}")
        print(f"   def solution(a, b):")
        print(f"       return a * b")

    def show_tests(self):
        """نمایش تست‌هایی که قرار است اجرا شوند"""
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
