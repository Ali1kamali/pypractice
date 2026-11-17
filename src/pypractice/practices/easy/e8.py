from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            (("  Hello World  ",), "Hello World"),
            (("Python",), "Python"),
            (("   Python Programming",), "Python Programming"),
            (("Python Programming   ",), "Python Programming"),
            (("   Hello Python   ",), "Hello Python"),
            (("",), ""),
            (("     ",), ""),
            (("  Hello   World  ",), "Hello   World"),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(f"{self.BLUE}{self.BOLD}=== Text Cleaner ==={self.RESET}")
        print(
            "Users sometimes enter unnecessary spaces at the beginning or "
            "end of their text.\n"
            "These extra spaces should be removed before storing the text "
            "in the database.\n\n"
            "Write a function that receives a string and removes all "
            "unnecessary spaces from its beginning and end.\n\n"
            "Return the cleaned string.\n\n"
            "Note: Do not remove spaces between words."
        )

    def help(self):
        print(
            f"💡 {self.yellow('Hint:')} "
            "Python has a built-in string method that removes whitespace "
            "from both ends of a string."
        )

        print(f"💡 {self.yellow('Example Solution:')}")
        print("   def solution(text):")
        print("       return text.strip()")

    def show_tests(self):
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
