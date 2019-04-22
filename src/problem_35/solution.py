"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the
values of the array so that all the Rs come first, the Gs come second, and the
Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
become ['R', 'R', 'R', 'G', 'G', 'B', 'B']
"""

import unittest
import random


def solve(inp_list):
    i = 0
    j = 0
    k = len(inp_list) - 1
    while j <= k:
        if inp_list[j] == 'R':
            inp_list[i], inp_list[j] = inp_list[j], inp_list[i]
            i += 1
            j += 1
        elif inp_list[j] == 'G':
            j += 1
        else:
            inp_list[j], inp_list[k] = inp_list[k], inp_list[j]
            k -= 1
    return inp_list    


class Tests(unittest.TestCase):
    def test_example1(self):
        given = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
        expected = ['R', 'R', 'R', 'G', 'G', 'B', 'B']
        self.assertEqual(solve(given), expected)

    def test_large_input(self):
        with open("large_input.txt") as f:
            given = [x for x in f.readline().split(",")]
        self.assertEqual(solve(given), sorted(given, reverse=True))
