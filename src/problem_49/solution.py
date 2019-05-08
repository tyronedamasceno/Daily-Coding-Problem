"""
Given an array of numbers, find the maximum sum of any contiguous subarray of
the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would
be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would
not take any elements.

Do this in O(N) time.
"""

import unittest

class Tests(unittest.TestCase):
    def test_example(self):
        inp = [34, -50, 42, 14, -5, 86]
        self.assertEqual(solve(inp), 137)
    
    def test_example2(self):
        inp = [-5, -1, -8, -9]
        self.assertEqual(solve(inp), 0)
