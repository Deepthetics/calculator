from math import log, sqrt, e, pi

from entities.equation import Equation
from entities.result import Result

from repositories.equation_repository import (
    equation_repository as default_equation_repository
)

from repositories.result_repository import (
    result_repository as default_result_repository
)


class CalculatorService:
    """Luokka, joka vastaa sovelluslogiikasta.

    Attributes:
        last_result: Result-luokan olio, joka kuvaa viimeksi laskettua tulosta.
        equation_repository: Vapaaehtoinen, oletusarvoisesti EquationRepository-luokan olio.
        result_repository: ...
    """

    def __init__(
        self, 
        equation_repository=default_equation_repository, 
        result_repository=default_result_repository
    ):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan olion.

        Args:
            equation_repository: Vapaaehtoinen, oletusarvoisesti EquationRepository-luokan olio.
            result_repository: ...
        """

        self._last_result = Result(value=0)
        self._equation_repository = equation_repository
        self._result_repository = result_repository

    def calculate(self, expression):
        """Laskee lausekkeen arvon.

        Args:
            expression: Merkkijonoarvo, joka kuvaa lauseketta.

        Returns:
            Palauttaa lasketun lausekkeen arvon.
            Jos lauseketta ei voida laskea, palauttaa False.
        """

        try:
            result = eval(expression)
            self._store_equation(Equation(expression, result))
            self._last_result = Result(value=result)
            return result
        except (NameError, SyntaxError):
            return False
    
    def _store_equation(self, equation):
        """Tallettaa lasketusta lausekkeesta uuden merkinnän laskuhistoriaan.

        Args:
            equation: Equation-luokan olio.
        """
        self._equation_repository.store(equation)

    def get_all_equations(self):
        """Palauttaa laskuhistorian.

        Returns:
            Palauttaa Equations-olioita sisältävän listan.
        """
        return self._equation_repository.get_all()

    def delete_all_equations(self):
        """Alustaa laskuhistorian.
        """
        self._equation_repository.delete_all()

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
