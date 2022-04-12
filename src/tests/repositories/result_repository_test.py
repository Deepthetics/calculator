import unittest
from repositories.result_repository import result_repository


class TestResultRepository(unittest.TestCase):
    def setUp(self):
        result_repository.clear()
    
    def test_write(self):
        pass
