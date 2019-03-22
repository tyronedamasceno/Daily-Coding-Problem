"""
Problem from day 22/03/2019

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

import unittest

def solve(inp_list=None):
    if not inp_list:
        return 1
    s = set(inp_list)
    minimum = min(s)
    for x in range(1, len(inp_list) + 1):
        if not x in s:
            return x


class Tests(unittest.TestCase):
    def test_example_1(self):
        ans = solve([3, 4, -1, 1])
        self.assertEqual(ans, 2)
    
    def test_example_2(self):
        ans = solve([1, 2, 0])
        self.assertEqual(ans, 3)

    def test_empty_input(self):
        ans1 = solve([])
        ans2 = solve()
        self.assertEqual(ans1, 1)
        self.assertEqual(ans2, 1)

    def test_with_large_input(self):
        """This input is a shuffled array from 0 to 99999"""
        with open("large_input.txt") as f:
            l = [int(x) for x in f.readline().split(",")]
        ans = solve(l)
        self.assertEqual(ans, 100000)
