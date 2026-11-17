from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            ((6, 2), 3),
            ((10, 5), 2),
            ((7, 1), 7),
            ((0, 4), 0),
            ((-8, 2), -4),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(
            f"{self.BLUE}{self.BOLD}=== Exercise 4: Divide Two Numbers ==={self.RESET}")
        print("Write a function that receives two numbers and returns their quotient.\n")

    def help(self):
        """توضیحات تکمیلی و یک نمونه از جواب درست"""

        print(f"💡 {self.yellow("Hint:")} You can use the '/' operator.")
        print(f"💡 {self.yellow("Example Solution:")}")
        print(f"   def solution(a, b):")
        print(f"       return a / b")

    def show_tests(self):
        """نمایش تست‌هایی که قرار است اجرا شوند"""
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
