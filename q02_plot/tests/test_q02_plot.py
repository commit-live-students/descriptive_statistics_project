import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from q02_plot.build import plot

class TestLoad_distplot(TestCase):
    def test_plot(self):
        plots = plot()
        self.assertTrue(True)