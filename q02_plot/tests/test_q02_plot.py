from unittest import TestCase
from q02_plot.build import plot

class TestLoad_distplot(TestCase):
    def test_plot(self):
        plots = plot()
        self.assertTrue(True)