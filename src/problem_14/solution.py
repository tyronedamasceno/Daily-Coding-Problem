"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using
a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import unittest
import random
from math import sqrt


def estimate():
    inside = 0
    for i in range(10000):
        x = random.random()
        y = random.random()
        k = sqrt(x**2+y**2)
        if k <= 0.5:
            inside += 1
    return inside/1000


class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(estimate(), 3.141)
