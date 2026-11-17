# check password power

from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            (("Strong123!",), True),
            (("Abcdef12@",), True),
            (("Python123#",), True),
            (("Abcdefgh1؟",), True),
            (("Abcdefgh1'",), True),
            (("Abcdef1!",), False),
            (("abcdef123!",), False),
            (("ABCDEFG123!",), False),
            (("Abcdefghi!",), False),
            (("Abcdef123",), False),
            (("Ab1!",), False),
            (("123456789!",), False),
            (("",), False),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(f"{self.BLUE}{self.BOLD}=== Password Strength Checker ==={self.RESET}")
        print(
            "Password security is important for protecting user accounts.\n\n"
            "Write a function that receives a password and checks "
            "whether it is strong or weak.\n\n"
            "A strong password must meet ALL the following requirements:\n\n"
            "1. Its length must be greater than 8 characters.\n"
            "2. It must contain at least one lowercase letter (a-z).\n"
            "3. It must contain at least one uppercase letter (A-Z).\n"
            "4. It must contain at least one digit (0-9).\n"
            "5. It must contain at least one special character from:\n"
            "   !@#$%^&*()_-+=: '\"|؟/.,\n\n"
            "Return True if the password is strong.\n"
            "Otherwise, return False."
        )

    def help(self):
        print(
            f"💡 {self.yellow('Hint:')} "
            "Use len(), any(), islower(), isupper(), and isdigit() "
            "to check the password requirements."
        )

        print(f"💡 {self.yellow('Example Solution:')}")
        print("   def solution(password):")
        print("       special = '!@#$%^&*()_-+=: ' + chr(39) + chr(34) + '|؟/.,'")
        print("       return (")
        print("           len(password) > 8")
        print("           and any(c.islower() and c.isascii() for c in password)")
        print("           and any(c.isupper() and c.isascii() for c in password)")
        print("           and any(c.isdigit() and c.isascii() for c in password)")
        print("           and any(c in special for c in password)")
        print("       )")

    def show_tests(self):
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
