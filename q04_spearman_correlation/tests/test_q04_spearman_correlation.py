from unittest import TestCase
from ..build import spearman_correlation
from inspect import getfullargspec


class TestLoad_regression_plot(TestCase):
    def test_correlation(self):

        # Input parameters tests
        args = getfullargspec(spearman_correlation).args
        args_default = getfullargspec(spearman_correlation).defaults
        self.assertEqual(len(args), 0, "Expected arguments %d, Given %d" % (0, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return type tests
        spear_corr = spearman_correlation()
        self.assertIsInstance(spear_corr, float, "Expected data type for `Spearman correlation` is float you are returning\
         %s" % (type(spear_corr)))

        # Return value tests
        self.assertAlmostEqual(spearman_correlation(), 0.0485967326141, 3, "Return `Spearman correlation` value does not match\
         expected value")
