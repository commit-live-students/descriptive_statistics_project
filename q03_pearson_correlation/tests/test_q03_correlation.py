from unittest import TestCase
from q03_pearson_correlation.build import correlation

class TestLoad_regression_plot(TestCase):
    def test_correlation(self):
        self.assertAlmostEqual(correlation(), 0.0487782084064, places=3)