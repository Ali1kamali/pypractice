from ...base import ExerciseTemplate
from collections import Counter
from datetime import datetime


class Exercise(ExerciseTemplate):
    def __init__(self):
        self._tests = [
            (
                ([
                    {"timestamp": "2026-11-18 10:00:00",
                        "level": "INFO", "message": "Server started"},
                    {"timestamp": "2026-11-18 10:01:00", "level": "ERROR",
                        "message": "Database connection failed"},
                    {"timestamp": "2026-11-18 10:02:00",
                        "level": "INFO", "message": "Server started"},
                    {"timestamp": "2026-11-18 10:03:00",
                        "level": "WARNING", "message": "High memory usage"},
                ],),
                {
                    "total": 4,
                    "levels": {"INFO": 2, "WARNING": 1, "ERROR": 1},
                    "duplicate_messages": 1,
                    "most_common_message": "Server started",
                    "last_log": {
                        "timestamp": "2026-11-18 10:03:00",
                        "level": "WARNING",
                        "message": "High memory usage"
                    }
                }
            ),
            (
                ([],),
                {
                    "total": 0,
                    "levels": {"INFO": 0, "WARNING": 0, "ERROR": 0},
                    "duplicate_messages": 0,
                    "most_common_message": None,
                    "last_log": None
                }
            ),
            (
                ([
                    {"timestamp": "2026-11-18 10:00:00",
                        "level": "INFO", "message": "Started"},
                ],),
                {
                    "total": 1,
                    "levels": {"INFO": 1, "WARNING": 0, "ERROR": 0},
                    "duplicate_messages": 0,
                    "most_common_message": "Started",
                    "last_log": {
                        "timestamp": "2026-11-18 10:00:00",
                        "level": "INFO",
                        "message": "Started"
                    }
                }
            ),
            (
                ([
                    {"timestamp": "2026-11-18 10:00:00",
                        "level": "ERROR", "message": "Connection failed"},
                    {"timestamp": "2026-11-18 10:01:00",
                        "level": "ERROR", "message": "Connection failed"},
                    {"timestamp": "2026-11-18 10:02:00",
                        "level": "ERROR", "message": "Connection failed"},
                ],),
                {
                    "total": 3,
                    "levels": {"INFO": 0, "WARNING": 0, "ERROR": 3},
                    "duplicate_messages": 1,
                    "most_common_message": "Connection failed",
                    "last_log": {
                        "timestamp": "2026-11-18 10:02:00",
                        "level": "ERROR",
                        "message": "Connection failed"
                    }
                }
            ),
            (
                ([
                    {"timestamp": "2026-11-18 10:00:00",
                        "level": "INFO", "message": "A"},
                    {"timestamp": "2026-11-18 10:01:00",
                        "level": "WARNING", "message": "B"},
                    {"timestamp": "2026-11-18 10:02:00",
                        "level": "ERROR", "message": "C"},
                    {"timestamp": "2026-11-18 10:03:00",
                        "level": "INFO", "message": "D"},
                ],),
                {
                    "total": 4,
                    "levels": {"INFO": 2, "WARNING": 1, "ERROR": 1},
                    "duplicate_messages": 0,
                    "most_common_message": "A",
                    "last_log": {
                        "timestamp": "2026-11-18 10:03:00",
                        "level": "INFO",
                        "message": "D"
                    }
                }
            ),
            (
                ([
                    {"timestamp": "2026-11-18 10:00:00",
                        "level": "INFO", "message": "A"},
                    {"timestamp": "2026-11-18 10:01:00",
                        "level": "ERROR", "message": "B"},
                    {"timestamp": "2026-11-18 10:02:00",
                        "level": "WARNING", "message": "A"},
                    {"timestamp": "2026-11-18 10:03:00",
                        "level": "ERROR", "message": "B"},
                ],),
                {
                    "total": 4,
                    "levels": {"INFO": 1, "WARNING": 1, "ERROR": 2},
                    "duplicate_messages": 2,
                    "most_common_message": "A",
                    "last_log": {
                        "timestamp": "2026-11-18 10:03:00",
                        "level": "ERROR",
                        "message": "B"
                    }
                }
            ),
            (
                ([
                    {"timestamp": "2026-11-18 10:05:00",
                        "level": "INFO", "message": "New event"},
                    {"timestamp": "2026-11-18 10:01:00",
                        "level": "ERROR", "message": "Old event"},
                    {"timestamp": "2026-11-18 10:03:00",
                        "level": "WARNING", "message": "Middle event"},
                ],),
                {
                    "total": 3,
                    "levels": {"INFO": 1, "WARNING": 1, "ERROR": 1},
                    "duplicate_messages": 0,
                    "most_common_message": "New event",
                    "last_log": {
                        "timestamp": "2026-11-18 10:05:00",
                        "level": "INFO",
                        "message": "New event"
                    }
                }
            ),
            (
                ([
                    {"timestamp": "2026-11-18 10:00:00",
                        "level": "INFO", "message": "A"},
                    {"timestamp": "2026-11-18 10:00:00",
                        "level": "ERROR", "message": "B"},
                ],),
                {
                    "total": 2,
                    "levels": {"INFO": 1, "WARNING": 0, "ERROR": 1},
                    "duplicate_messages": 0,
                    "most_common_message": "A",
                    "last_log": {
                        "timestamp": "2026-11-18 10:00:00",
                        "level": "ERROR",
                        "message": "B"
                    }
                }
            ),
        ]

    @property
    def tests(self):
        return self._tests

    def about(self):
        print(f"{self.BLUE}{self.BOLD}=== System Log Analyzer ==={self.RESET}")
        print(
            "Design a log analyzer for a software system.\n\n"
            "Each log entry is a dictionary containing three fields:\n"
            "- timestamp: The date and time of the event.\n"
            "- level: The severity level (INFO, WARNING, or ERROR).\n"
            "- message: A description of the event.\n\n"
            "Write a function named analyze_logs(logs) that receives "
            "a list of log entries and returns a dictionary containing:\n\n"
            "1. total: The total number of log entries.\n"
            "2. levels: A dictionary containing the number of entries "
            "for each severity level (INFO, WARNING, ERROR).\n"
            "3. duplicate_messages: The number of distinct messages "
            "that appear more than once.\n"
            "4. most_common_message: The message that appears most often.\n"
            "5. last_log: The log entry with the latest timestamp.\n\n"
            "Important Rules:\n"
            "- Timestamps use the format YYYY-MM-DD HH:MM:SS.\n"
            "- The input contains valid log dictionaries and valid severity levels.\n"
            "- If multiple messages have the same highest frequency, "
            "return the one that appeared first.\n"
            "- If multiple logs have the same latest timestamp, "
            "return the last one in the input list.\n"
            "- If the input is empty, return 0 for total and all level counts, "
            "and None for most_common_message and last_log.\n"
            "- duplicate_messages counts distinct repeated messages, "
            "not the total number of extra occurrences."
        )

    def help(self):
        print(
            f"💡 {self.yellow('Hint:')} "
            "Use collections.Counter to count message frequencies.\n"
            "Use datetime.strptime() to convert timestamp strings "
            "into datetime objects.\n"
            "Consider using Counter.most_common() to find the most frequent message.\n"
            "You can use a dictionary to count each severity level."
        )

        print(f"💡 {self.yellow('Example Solution:')}")
        print("   from collections import Counter")
        print("   from datetime import datetime")
        print("")
        print("   def solution(logs):")
        print("       levels = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}")
        print("       messages = Counter()")
        print("")
        print("       for log in logs:")
        print("           levels[log['level']] += 1")
        print("           messages[log['message']] += 1")
        print("")
        print("       most_common = messages.most_common(1)")
        print("")
        print("       last_log = None")
        print("       if logs:")
        print("           last_log = max(")
        print("               logs,")
        print("               key=lambda log: datetime.strptime(")
        print("                   log['timestamp'], '%Y-%m-%d %H:%M:%S'")
        print("               )")
        print("           )")
        print("")
        print("       return {")
        print("           'total': len(logs),")
        print("           'levels': levels,")
        print("           'duplicate_messages': sum(1 for count in messages.values() if count > 1),")
        print(
            "           'most_common_message': most_common[0][0] if most_common else None,")
        print("           'last_log': last_log")
        print("       }")

    def show_tests(self):
        self._show_test_value(self.tests)

    def check(self, solution):
        self._check_function(solution)
