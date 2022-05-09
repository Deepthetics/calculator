from pathlib import Path
from config import RESULTS_FILE_PATH


class ResultRepository:
    """Luokka, joka vastaa laskimen muistiin ja Result-olioihin liittyvistä tiedosto-operaatioista.

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

    def store(self, result):
        """Tallettaa tuloksen tiedostoon.

        Args:
            result: Result-luokan olio.
        """
        with open(self._file_path, "a", encoding="utf-8") as file:
            row = f"{result.value}"
            file.write(row+"\n")

    def recall(self):
        """Palauttaa tiedoston viimeisimmän rivin.

        Returns:
            Palauttaa tuloksen merkkijonoarvona.
        """
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            results = file.readlines()

            if not results:
                return False
            return results[-1]

    def delete_all(self):
        """Alustaa tiedoston.
        """
        with open(self._file_path, "w", encoding=("utf-8")) as file:
            file.truncate()


result_repository = ResultRepository(RESULTS_FILE_PATH)
