from math import sqrt
from entities.result import Result
from repositories.result_repository import (
    result_repository as default_result_repository)


class CalculatorService:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, result_repository=default_result_repository):
        self._last_result = Result(value=0)
        self._result_repository = result_repository

    def calculate(self, expression):
        """Laskee lausekkeen arvon.

        Args:
            expression: Merkkijonoarvo, joka kuvaa lauseketta.

        Returns:
            Palauttaan lasketun lausekkeen arvon.
            Jos lauseketta ei voida laskea, palauttaa False.
        """

        try:
            result = eval(expression)
            self._last_result = Result(value=result)
            return result
        except (NameError, SyntaxError):
            return False

    def memory_store(self):
        self._result_repository.write(self._last_result)

    def memory_recall(self):
        last = self._result_repository.read_last()
        if last:
            return last
        return False

    def memory_clear(self):
        self._result_repository.clear()


calculator_service = CalculatorService()
