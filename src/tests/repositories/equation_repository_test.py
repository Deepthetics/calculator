import unittest
from repositories.equation_repository import equation_repository
from entities.equation import Equation


class TestEquationRepository(unittest.TestCase):
    def setUp(self):
        equation_repository.delete_all()
        self.equation_a = Equation("5+5", 10)
        self.equation_b = Equation("25.5-5", 20)

    def test_store_writes_to_file(self):
        equation_repository.store(self.equation_a)
        equations = equation_repository.get_all()
        self.assertEqual(int(equations[0].result), 10)

    def test_get_all_returns_all_equations(self):
        equation_repository.store(self.equation_a)
        equation_repository.store(self.equation_b)
        equations = equation_repository.get_all()
        self.assertEqual(int(equations[0].result), 10)
        self.assertEqual(int(equations[1].result), 20)

    def test_delete_all_formats_file(self):
        equation_repository.store(self.equation_a)
        equation_repository.store(self.equation_b)
        equation_repository.delete_all()
        self.assertEqual(equation_repository.get_all(), False)
