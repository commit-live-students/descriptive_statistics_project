from unittest import TestCase
from ..build import correlation
from inspect import getfullargspec


class TestLoad_regression_plot(TestCase):
    def test_correlation(self):
     
        # Input parameters tests
        args = getfullargspec(correlation).args
        args_default = getfullargspec(correlation).defaults
        self.assertEqual(len(args), 0, "Expected arguments %d, Given %d" % (0, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return type tests
        corr = correlation()
        self.assertIsInstance(corr, float,
                              "Expected data type for Pearson correlation is float you are returning %s" % (type(corr)))

        # Return value tests
        self.assertAlmostEqual(correlation(), 0.0487782084064, 3, "Return `Pearson correlation` value does not match\
         expected value")
