import pandas as pd
from unittest import TestCase
from q01_calculate_statistics.build import calculate_statistics

class TestLoad_distplot(TestCase):
    def test_calculate_statistics(self):
        mean, median, mode = calculate_statistics()
        self.assertAlmostEqual(mean, 185479.51124002901, places=2)
        self.assertAlmostEqual(median, 167500.0, places=1)
        self.assertAlmostEqual(pd.Series(mode).values, 140000)