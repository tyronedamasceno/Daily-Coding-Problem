"""
You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two walls get
filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1)
space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2
in the second, and 3 in the fourth index (we cannot hold 5 since it would run
off to the left), so we can trap 8 units of water.
"""

import unittest

def solve(l):
    if len(l) < 2:
        return 0
    height = min(l[0], l[-1])
    ans = 0
    for i in l[1:-1]:
        ans += max(0, height-i)
    return ans


class Tests(unittest.TestCase):
    def test_example1(self):
        l = [2, 1, 2]
        self.assertEqual(solve(l), 1)

    def test_example2(self):
        l = [3, 0, 1, 3, 0, 5]
        self.assertEqual(solve(l), 8)
