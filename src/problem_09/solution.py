"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

import unittest



class Tests(unittest.TestCase):
    def test_example_1(self):
        ans = solve([2, 4, 6, 2, 5])
        self.assertEqual(ans, 13)
    
    def test_example_2(self):
        ans = solve([5, 1, 1, 5])
        self.assertEqual(ans, 10)
