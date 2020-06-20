import math
import unittest

from app.GeometricMean import GeometricMean


class TestGeometricMean(unittest.TestCase):
    def test_get_computes_the_geometric_mean_data(self):
        expected = 16.917
        data = [ 8, 12, 16, 22, 41 ]

        actual = GeometricMean.get(data)

        self.assertTrue(math.isclose(actual, expected, abs_tol=0.001), f'expected {expected}, got {actual}')
