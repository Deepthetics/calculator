import unittest
from services.stats_service import StatsService


class TestStatsService(unittest.TestCase):
    def setUp(self):
        self.stats_service = StatsService()
    
    def test_normal_cdf_with_valid_input(self):
        valid_input_1 = ["0", "0", "1"]
        valid_input_2 = ["-2", "-1", "2"]
        self.assertEqual(self.stats_service.normal_cdf(valid_input_1[0], valid_input_1[1], valid_input_1[2]), 0.5)
        self.assertEqual(self.stats_service.normal_cdf(valid_input_2[0], valid_input_2[1], valid_input_2[2]), 0.30854)
    def test_normal_cdf_with_invalid_input(self):
        invalid_input_1 = ["0", "0", "0"]
        invalid_input_2 = ["-2", "-1", "-2"]
        self.assertEqual(self.stats_service.normal_cdf(invalid_input_1[0], invalid_input_1[1], invalid_input_1[2]), False)
        self.assertEqual(self.stats_service.normal_cdf(invalid_input_2[0], invalid_input_2[1], invalid_input_2[2]), False)
