"""
Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import unittest

def solve(inp_list=None):
    if not inp_list:
        return 0


class Tests(unittest.TestCase):
    def test_example(self):
        x = [(30, 75), (0, 50), (60, 150)]
        self.assertEqual(solve(x), 2)

    def test_empty_lists(self):
        self.assertEqual(solve(), 0)
        self.assertEqual(solve([]), 0)
