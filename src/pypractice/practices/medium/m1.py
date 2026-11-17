# create random password

from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            (("Strong123!",), "Strong123!"),
            (("Abcdef12@",), "Abcdef12@"),
            (("Python123#",), "Python123#"),
            (("Abcdefgh1؟",), "Abcdefgh1؟"),
            (("Abcdefgh1'",), "Abcdefgh1'"),
            (("Abcdef1!",), -1),
            (("abcdef123!",), -1),
            (("ABCDEFG123!",), -1),
            (("Abcdefghi!",), -1),
            (("Abcdef123",), -1),
            (("Ab1!",), -1),
            (("123456789!",), -1),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(f"{self.BLUE}{self.BOLD}=== Strong Password Validator ==={self.RESET}")
        print(
            "To improve user experience and security, help users "
            "identify strong passwords.\n\n"
            "Write a function that receives a password and checks "
            "whether it meets all the following requirements:\n\n"
            "1. The password must be longer than 8 characters.\n"
            "2. It must contain at least one lowercase letter (a-z).\n"
            "3. It must contain at least one uppercase letter (A-Z).\n"
            "4. It must contain at least one digit (0-9).\n"
            "5. It must contain at least one special character from:\n"
            "   !@#$%^&*()_-+=: '\"|؟ /.,\n\n"
            "If all requirements are met, return the original password.\n"
            "Otherwise, return -1."
        )

    def help(self):
        print(
            f"💡 {self.yellow('Hint:')} "
            "Use len() to check the password length and any() "
            "to search for specific character types.\n"
            "You can use separate conditions for lowercase letters, "
            "uppercase letters, digits, and special characters."
        )

        print(f"💡 {self.yellow('Example Solution:')}")
        print("   def solution(password):")
        print("       if len(password) <= 8:")
        print("           return -1")
        print("")
        print("       special_chars = '!@#$%^&*()_-+=:' + chr(39) + chr(34) + '|؟/.,'")
        print("       has_lower = any(c.islower() and c.isascii() for c in password)")
        print("       has_upper = any(c.isupper() and c.isascii() for c in password)")
        print("       has_digit = any(c.isdigit() and c.isascii() for c in password)")
        print("       has_special = any(c in special_chars for c in password)")
        print("")
        print("       if has_lower and has_upper and has_digit and has_special:")
        print("           return password")
        print("")
        print("       return -1")

    def show_tests(self):
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
