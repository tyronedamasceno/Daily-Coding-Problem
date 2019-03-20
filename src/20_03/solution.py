"""
Problem from day 20/03/2019

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

import unittest
import functools


def mutiply_items_from_list(inp_list):
    return functools.reduce(lambda x, y: x*y, inp_list)


def solve(inp_list):
    product = mutiply_items_from_list(inp_list)
    return [product//x for x in inp_list]


class Tests(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            solve([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24]
        )

    def test_example2(self):
        self.assertEqual(
            solve([3, 2, 1]), [2, 3, 6]
        )
