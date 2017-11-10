import numpy
from inspect import getfullargspec
from unittest import TestCase
from ..build import calculate_statistics


class TestLoad_distplot(TestCase):
    def test_calculate_statistics(self):
        
        # Input parameters tests
        args = getfullargspec(calculate_statistics).args
        args_default = getfullargspec(calculate_statistics).defaults
        self.assertEqual(len(args), 0, "Expected arguments %d, Given %d" % (0, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return type tests
        mean, median, mode = calculate_statistics()
        self.assertIsInstance(mean, float, "Expected data type for mean is float you are returning %s" % (type(mean)))
        self.assertIsInstance(median, float,
                              "Expected data type for median is float you are returning %s" % (type(median)))
        self.assertIsInstance(mode, numpy.int64,
                              "Expected data type for mode is numpy.int64 you are returning %s" % (type(mode)))

        # Return value tests
        self.assertAlmostEqual(mean, 185479.51124002901, 2, "Return `mean` value does not match expected value")
        self.assertAlmostEqual(median, 167500.0, 1, "Return `median` value does not match expected value")
        self.assertAlmostEqual(mode, 140000, "Return `mode` value does not match expected value")
