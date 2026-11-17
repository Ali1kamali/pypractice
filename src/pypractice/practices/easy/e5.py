from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            ((18,), 18),
            ((19,), 19),
            ((25,), 25),
            ((0,), -1),
            ((17,), -1),
            ((1,), -1),
            ((-5,), -1),
            ((1818,), 1818),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(f"{self.BLUE}{self.BOLD}=== Age Validator ==={self.RESET}")
        print(
            "Write a function that receives a user's age.\n"
            "If the age is 18 or greater, return the age itself.\n"
            "Otherwise, return -1.\n"
        )

    def help(self):
        print(f"💡 {self.yellow('Hint:')} Use an if statement to check whether the age is greater than or equal to 18.")

        print(f"💡 {self.yellow('Example Solution:')}")
        print("   def solution(age):")
        print("       if age >= 18:")
        print("           return age")
        print("       return -1")

    def show_tests(self):
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
