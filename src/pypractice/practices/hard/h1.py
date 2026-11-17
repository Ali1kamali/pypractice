from ...base import ExerciseTemplate


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            (("abc",), 1),
            (("Abc123",), 3),
            (("Abc123!",), 4),
            (("Abc123!xyz12",), 5),
            (("Abc123!xyz123456",), 6),
            (("",), 0),
            (("123456789",), 1),
            (("ABCDEFGHIJKL",), 2),
            (("abcdefghijkl",), 2),
            (("Abcdefghijkl",), 3),
            (("Abcdefghijkl!",), 4),
            (("1234567890123456",), 3),
            (("Abcdefghijkl123456",), 5),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(f"{self.BLUE}{self.BOLD}=== Password Strength Analyzer ==={self.RESET}")
        print(
            "Design a password strength analyzer for a user registration system.\n\n"
            "Write a function that receives a password and calculates "
            "its security score based on the following rules:\n\n"
            "1. At least one lowercase English letter (a-z): +1 point.\n"
            "2. At least one uppercase English letter (A-Z): +1 point.\n"
            "3. At least one digit (0-9): +1 point.\n"
            "4. At least one special character: +1 point.\n"
            "5. Password length of at least 12 characters: +1 point.\n"
            "6. Password length of at least 16 characters: +1 additional point.\n\n"
            "Special characters include:\n"
            "!@#$%^&*()_-+=: '\"|؟/.,\n\n"
            "Return the final score as an integer between 0 and 6.\n\n"
            "Note: Each character category can only earn points once, "
            "regardless of how many times its characters appear."
        )

    def help(self):
        print(
            f"💡 {self.yellow('Hint:')} "
            "Use any() to check whether a character category exists "
            "in the password.\n"
            "Use string methods to identify lowercase letters, "
            "uppercase letters, and digits.\n"
            "Use a variable to keep track of the score."
        )

        print(f"💡 {self.yellow('Example Solution:')}")
        print("   def solution(password):")
        print("       score = 0")
        print("")
        print("       if any(c.islower() and c.isascii() for c in password):")
        print("           score += 1")
        print("")
        print("       if any(c.isupper() and c.isascii() for c in password):")
        print("           score += 1")
        print("")
        print("       if any(c.isdigit() and c.isascii() for c in password):")
        print("           score += 1")
        print("")
        print("       special = '!@#$%^&*()_-+=: ' + chr(39) + chr(34) + '|؟/.,'")
        print("       if any(c in special for c in password):")
        print("           score += 1")
        print("")
        print("       if len(password) >= 12:")
        print("           score += 1")
        print("")
        print("       if len(password) >= 16:")
        print("           score += 1")
        print("")
        print("       return score")

    def show_tests(self):
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
