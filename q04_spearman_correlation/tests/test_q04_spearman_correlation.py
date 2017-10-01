import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from q04_spearman_correlation.build import spearman_correlation

class TestLoad_regression_plot(TestCase):
    def test_correlation(self):
        self.assertAlmostEqual(spearman_correlation(), 0.0485967326141, places=3)