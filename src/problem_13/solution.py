"""
Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""

import unittest


class Tests(unittest.TestCase):
    def test_example(self):
        ans = solve('abcba', 2)
        self.assertEqual(ans, 3)
