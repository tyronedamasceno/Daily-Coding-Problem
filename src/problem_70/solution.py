"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

import unittest


def solve(n):
    i = 0
    while n > 0:
        i += 1
        if sum_digits(i) == 10:
            n -= 1
    return i


def sum_digits(n):
    s = 0
    while n > 0:
        s += (n % 10)
        n //= 10
    return s


class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(1), 19)

    def test_example2(self):
        self.assertEqual(solve(2), 28)

