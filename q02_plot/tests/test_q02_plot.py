from inspect import getfullargspec
from ..build import plot
from unittest import TestCase


class TestLoad_distplot(TestCase):
    def test_plot(self):  # Input parameters tests
        args = getfullargspec(plot)
        self.assertEqual(len(args[0]), 0, "Expected arguments %d, Given %d" % (0, len(args[0])))

    def test_plot_default(self):  # Input parameters defaults
        args = getfullargspec(plot)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
        # Nothing to check here

        # Return value tests
        # Nothing to test here
