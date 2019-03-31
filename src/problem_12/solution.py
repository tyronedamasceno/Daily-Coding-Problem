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

"""
This solution solves efficiently the original problem (1 or 2 steps allowed).
It uses dynamic programming and memoization techniques and has linear time complexity.
"""
def solve(n, d):
    if d.get(n) is not None:
        return d.get(n)
    x = solve(n-1, d) + solve(n-2, d)
    d[n] = x
    return x


class Tests(unittest.TestCase):
    def test_n_zero(self):
        d = {0:0, 1:1, 2:2}
        self.assertEqual(solve(0, d), 0)

    def test_n_one(self):
        d = {0:0, 1:1, 2:2}
        self.assertEqual(solve(1, d), 1)
    
    def test_n_two(self):
        d = {0:0, 1:1, 2:2}
        self.assertEqual(solve(2, d), 2)

    def test_n_three(self):
        d = {0:0, 1:1, 2:2}
        self.assertEqual(solve(3, d), 3)

    def test_n_four(self):
        d = {0:0, 1:1, 2:2}
        self.assertEqual(solve(4, d), 5)

    def test_n_98(self):
        d = {0:0, 1:1, 2:2}
        self.assertEqual(solve(98, d), 218922995834555169026)
