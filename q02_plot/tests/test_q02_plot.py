from inspect import getargspec
from ..build import plot
from unittest import TestCase

class TestLoad_distplot(TestCase):
    def test_plot(self):
        args = getargspec(plot)

        # Input parameters tests
        self.assertEqual(len(args[0]), 0, "Expected arguments %d, Given %d" % (0,len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")
