
import unittest
from services.calculator_service import CalculatorService

class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.calculator_service = CalculatorService()
    
    def test_calculate_with_valid_input(self):
        valid_expression = "2*4.5/(5-abs(-2))+sqrt((9%5))**3"
        self.assertEqual(self.calculator_service.calculate(valid_expression), 11.0)

    def test_calculate_with_unvalid_input(self):
        invalid_expression = "invalid"
        self.assertEqual(self.calculator_service.calculate(invalid_expression), False)