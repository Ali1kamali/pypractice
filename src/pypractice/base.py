from abc import ABC, abstractmethod


class ExerciseTemplate(ABC):
    """
    این کلاس به عنوان یک قرارداد عمل می‌کند. 
    هر کلاسی که از این ارث‌بری کند، مجبور است متدهای زیر را پیاده‌سازی کند.
    """
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    def _check_function(self, user_solution) -> None:
        passed = 0

        for index, (inputs, expected) in enumerate(self.tests, 1):

            try:
                result = user_solution(*inputs)

                if result == expected:
                    passed += 1
                    self._pass(index)
                else:
                    self.failed(index)

            except Exception as error:
                print(f"Test {index}: ⚠️ ERROR - {error}")

        print(f"\n{passed}/{len(self.tests)} tests passed.")
        print()

    def _show_test_value(self , tests):
        print("--- Upcoming Tests ---")

        for i, (inputs, expected) in enumerate(tests, 1):
            input_str = ", ".join(map(str, inputs))
            print(f"Test {i}: Input({input_str}) -> Expected: {expected}")

        print("----------------------")
        print()

    def _pass(self, index):
        print(f"Test {index}: ✅ PASS")

    def failed(self, index):
        print(f"Test {index}: ❌ FAILED")

    def yellow(self, input: str):
        return self.YELLOW + input + self.RESET

    def red(self, input: str):
        return self.RED + input + self.RESET

    def green(self, input: str):
        return self.GREEN + input + self.RESET

    def blue(self, input: str):
        return self.BLUE + input + self.RESET

    def bold(self, input: str):
        return self.BOLD + input + self.RESET

    @property
    @abstractmethod
    def tests(self) -> list:
        """باید لیستی از تست‌ها را برگرداند: [((input), expected), ...]"""
        pass

    @abstractmethod
    def about(self) -> str:
        """باید صورت سوال را چاپ کند"""
        pass

    @abstractmethod
    def help(self) -> str:
        """باید توضیحات متنی تمرین را برگرداند"""
        pass

    @abstractmethod
    def show_tests(self) -> None:
        """باید تست‌ها را برای کاربر پرینت کند"""
        pass

    @abstractmethod
    def check(self, user_solution) -> None:
        """باید منطق اجرای تست‌ها را داشته باشد"""
        pass
