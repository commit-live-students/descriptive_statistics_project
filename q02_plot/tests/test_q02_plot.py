from inspect import getfullargspec
from ..build import plot
from unittest import TestCase


class TestLoad_distplot(TestCase):
    def test_plot(self):
        
        # Input parameters tests
        args = getfullargspec(plot).args
        args_default = getfullargspec(plot).defaults
        self.assertEqual(len(args), 0, "Expected arguments %d, Given %d" % (0, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return data types
        # Nothing to check here

        # Return value tests
        # Nothing to test here
