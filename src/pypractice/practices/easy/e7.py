from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            ((True, False), True),
            ((False, False), False),
            ((True, True), True),
            ((False, True), False),
            ((True, False, True), True),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(
            f"{self.BLUE}{self.BOLD}=== Exercise: Logical Operators Check ==={self.RESET}")
        print("Write a function that takes multiple boolean values and returns the result of 'OR' operation for all of them.\n")

    def help(self):
        """توضیحات تکمیلی و یک نمونه از جواب درست"""

        print(f"💡 {self.yellow('Hint:')} Use the `or` operator. Remember that `a or b or c` returns `True` if at least one value is `True`.")
        print(f"💡 {self.yellow('Example Solution:')}")
        print(f"   def solution(*args):")
        print(f"       result = False")
        print(f"       for val in args:")
        print(f"           result = result or val")
        print(f"       return result")

    def show_tests(self):
        """نمایش تست‌هایی که قرار است اجرا شوند"""
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
