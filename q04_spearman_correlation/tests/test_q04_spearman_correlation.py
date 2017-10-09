from unittest import TestCase
from ..build import spearman_correlation
from inspect import getargspec


class TestLoad_regression_plot(TestCase):
    def test_correlation(self):
        spear_corr = spearman_correlation()
        args = getargspec(spearman_correlation)

        # Input parameters tests
        self.assertEqual(len(args[0]), 0, "Expected arguments %d, Given %d" % (0, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return type tests
        self.assertIsInstance(spear_corr, float, "Expected data type for `Spearman correlation` is float you are returning\
         %s" % (type(spear_corr)))

        # Return value tests
        self.assertAlmostEqual(spearman_correlation(), 0.0485967326141, 3, "Return `Spearman correlation` value does not match\
         expected value")
