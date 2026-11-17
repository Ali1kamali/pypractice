from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            (([1, 2, 3],), 6),
            (([10, -2, 5],), 13),
            (([0, 0, 0],), 0),
            (([],), 0),
            (([100],), 100),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(
            f"{self.BLUE}{self.BOLD}=== Exercise: Sum of List Elements ==={self.RESET}")
        print("Write a function that receives a list of numbers as an argument and returns the sum of all elements in that list.\n")

    def help(self):
        """توضیحات تکمیلی و یک نمونه از جواب درست"""

        print(f"💡 {self.yellow('Hint:')} You can use the built-in `sum()` function or a `for` loop to iterate through the list.")
        print(f"💡 {self.yellow('Example Solution 1 (using sum):')}")
        print(f"   def solution(numbers):")
        print(f"       return sum(numbers)")
        print(f"\n💡 {self.yellow('Example Solution 2 (using loop):')}")
        print(f"   def solution(numbers):")
        print(f"       total = 0")
        print(f"       for num in numbers:")
        print(f"           total += num")
        print(f"       return total")


    def show_tests(self):
        """نمایش تست‌هایی که قرار است اجرا شوند"""
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
