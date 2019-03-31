"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5},
you could climb 1, 3, or 5 steps at a time.
"""

import unittest

def solve(n):
    if n <= 2:
        return n
    return solve(n-1) + solve(n-2)


class Tests(unittest.TestCase):
    def test_n_zero(self):
        self.assertEqual(solve(0), 0)

    def test_n_one(self):
        self.assertEqual(solve(1), 1)
    
    def test_n_two(self):
        self.assertEqual(solve(2), 2)

    def test_n_three(self):
        self.assertEqual(solve(3), 3)

    def test_n_four(self):
        self.assertEqual(solve(4), 5)

    def test_n_98(self):
        self.assertEqual(solve(98), 218922995834555169026)
