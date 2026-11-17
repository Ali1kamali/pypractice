from dataclasses import dataclass
from typing import Literal

from .about import about as _about
from .help import help as _help
from .check import check as _check
from .show_tests import show_tests as _show_tests


@dataclass(frozen=True)
class Practice:
    dificult: Literal["easy", "medium", "hard"]
    number: int

    def about(self):
        return _about(self.dificult, self.number)

    def help(self):
        return _help(self.dificult, self.number)
    
    def show_test(self):
        return _show_tests(self.dificult, self.number)

    # with 's'
    def show_tests(self):
        return _show_tests(self.dificult, self.number)
    
    def check(self, solution):
        return _check(self.dificult, self.number, solution)
