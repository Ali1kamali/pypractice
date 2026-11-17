import importlib
import pkgutil
from typing import Type, Any
from ..base import ExerciseTemplate


class Engine:
    """
    موتور اصلی پکیج که وظیفه مدیریت تمرین‌ها را دارد.
    """

    def __init__(self):
        self.exercises = {}  # ساختاری برای ذخیره تمرین‌های پیدا شده

    def discover_exercises(self, package_path):
        """
        پیمایش پوشه‌ها و پیدا کردن تمام کلاس‌هایی که از ExerciseTemplate ارث برده‌اند.
        """
        # اینجا منطقی می‌نویسی که در پوشه‌های easy, medium, hard بچرخد
        # و هر ماژولی را که پیدا کرد، import کند.
        pass

    def get_exercise(self, category: str, exercise_id: str) -> ExerciseTemplate:
        """
        برگرداندن یک شیء از تمرین مورد نظر بر اساس دسته‌بندی و ID.
        """
        # مثلا: engine.get_exercise("easy", "e1")
        pass

    def run_check(self, exercise_instance: ExerciseTemplate, user_solution: Any):
        """
        اجرای منطق تست برای یک تمرین خاص.
        """
        try:
            exercise_instance.check(user_solution)
        except AttributeError:
            print("Error: This exercise does not support the 'check' method.")
        except Exception as e:
            print(f"An unexpected error occurred during execution: {e}")

    def run_show_tests(self, exercise_instance: ExerciseTemplate):
        """
        نمایش تست‌ها برای کاربر.
        """
        exercise_instance.show_tests()
