import unittest
from unittest import result
from repositories.result_repository import result_repository
from entities.result import Result


class TestResultRepository(unittest.TestCase):
    def setUp(self):
        result_repository.delete_all()
        self.result_a = Result(10)
        self.result_b = Result(20)

    def test_store_writes_to_file(self):
        result_repository.store(self.result_a)
        value = result_repository.recall()
        self.assertEqual(int(value), 10)

    def test_recall_returns_correct_value(self):
        result_repository.store(self.result_a)
        result_repository.store(self.result_b)
        value = result_repository.recall()
        self.assertEqual(int(value), 20)

    def test_delete_all_formats_file(self):
        result_repository.store(self.result_a)
        result_repository.store(self.result_b)
        result_repository.delete_all()
        self.assertEqual(result_repository.recall(), False)
