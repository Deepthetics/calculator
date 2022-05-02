from pathlib import Path
from config import EQUATIONS_FILE_PATH
from entities.equation import Equation


class EquationRepository:
    """Luokka, joka vastaa laskuhistoriaan ja Equations-olioihin liittyvistä tiedosto-operaatioista.

    Attributes:
        file_path: Merkkijonoarvo, joka kuvaa käytettävän tiedoston polkua.
    """

    def __init__(self, file_path):
        """Luokan konstruktori, joka luo uuden tiedosto-operaatioista vastaavan olion.

        Args:
            file_path: Merkkijonoarvo, joka kuvaa käytettävän tiedoston polkua.
        """

        self._file_path = file_path

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def store(self, equation):
        """Tallettaa laskuhistorian uuden merkinnän tiedostoon.

        Args:
            equation: Equation-luokan olio.
        """
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            row = f"{equation.expression};{equation.result}"
            file.write(row+"\n")

    def get_all(self):
        """Palauttaa laskuhistorian tiedostosta.

        Returns:
            Palauttaa Equations-olioita sisältävän listan.
        """
        self._ensure_file_exists()

        equations = []

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                attributes = row.split(";")
                expression = attributes[0]
                result = attributes[1]
                equations.append(Equation(expression, result))
            
            return equations

    def delete_all(self):
        """Alustaa laskuhistoriaa vastaavan tiedoston. 
        """
        with open(self._file_path, "w", encoding=("utf-8")) as file:
            file.truncate()
    

equation_repository = EquationRepository(EQUATIONS_FILE_PATH)
