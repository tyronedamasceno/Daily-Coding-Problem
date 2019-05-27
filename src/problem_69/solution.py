"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

import unittest


def solve(l):
    ans = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                ans = max(ans, l[i]*l[j]*l[k])
    return ans


class Tests(unittest.TestCase):
    def test_example(self):
        ans = solve([-10, -10, 5, 2])
        self.assertEqual(ans, 500)

    def test_return_zero(self):
        ans = solve([-1, 0, 1])
        self.assertEqual(ans, 0)

    def test_with_a_larger_list(self):
        l = [-68, -27, -89, 72, 73, 0, 4, -40, -21, -92]
        ans = solve(l)
        self.assertEqual(ans, 597724)

