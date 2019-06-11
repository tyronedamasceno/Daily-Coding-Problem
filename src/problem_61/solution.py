"""
Implement integer exponentiation. That is, implement the pow(x, y) function,
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

import unittest

def my_pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    tmp = my_pow(base, exp//2)
    if exp % 2 == 0:
        return tmp*tmp
    return tmp*tmp*base


class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(my_pow(2, 10), 1024)

    def test_exp_0(self):
        self.assertEqual(my_pow(2, 0), 1)

    def test_exp_1(self):
        self.assertEqual(my_pow(2, 1), 2)

