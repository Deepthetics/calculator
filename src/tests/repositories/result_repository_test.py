import unittest
from repositories.result_repository import result_repository
from entities.result import Result


class TestResultRepository(unittest.TestCase):
    def setUp(self):
        result_repository.clear()
        self.result_a = Result(10)
        self.result_b = Result(20)

    def test_write(self):
        result_repository.write(self.result_a)
        value = result_repository.read_last()
        self.assertEqual(value, "10")
    
    def test_read_last(self):
        result_repository.write(self.result_a)
        result_repository.write(self.result_b)
        value = result_repository.read_last()
        self.assertEqual(value, "20")
