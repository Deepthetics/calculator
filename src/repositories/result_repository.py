from pathlib import Path
from config import RESULTS_FILE_PATH
from entities.result import Result


class ResultRepository:
    """Luokka, joka vastaa tiedosto-operaatioista.

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
    
    def write(self, result):
        """Tallettaa viimeisimmän tuloksen tiedostoon.
        """
        with open(self._file_path, "w", encoding="utf-8") as file:
            row = f"{result.value};{result.id};{result.description}"
            file.write(row+"\n")

    def read_last(self):
        """Palauttaa tiedoston viimeisimmän rivin.
        """
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            results = file.readlines()
            if not results:
                return False
            parts = results[-1].split(";")
            return parts[0]

    def clear(self):
        """Alustaa tiedoston.
        """
        with open(self._file_path, "w") as file:
            file.truncate()


result_repository = ResultRepository(RESULTS_FILE_PATH)
