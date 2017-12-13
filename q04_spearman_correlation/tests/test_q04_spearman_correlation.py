from unittest import TestCase
from ..build import spearman_correlation
from inspect import getargspec


class TestLoad_regression_plot(TestCase):
    def test_correlation(self):  # Input parameters tests
        args = getargspec(spearman_correlation)
        self.assertEqual(len(args[0]), 0, "Expected arguments %d, Given %d" % (0, len(args[0])))

    def test_correlation_default(self):  # Input parameters default
        args = getargspec(spearman_correlation)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_correlation_result_type(self):    # Return type tests
        spear_corr = spearman_correlation()
        self.assertIsInstance(spear_corr, float, "Expected data type for `Spearman correlation` is float you are returning\
         %s" % (type(spear_corr)))

    def test_correlation_result_values(self):  # Return value tests
        spear_corr = spearman_correlation()
        self.assertAlmostEqual(spearman_correlation(), 0.0485967326141, 3, "Return `Spearman correlation` value does not match\
         expected value")
