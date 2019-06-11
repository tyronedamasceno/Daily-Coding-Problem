"""
Given an array of integers, write a function to determine whether the array
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we
can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify
any one element to get a non-decreasing array.
"""

import unittest


def solve(seq):
    counter = 0
    for i in range(1, len(seq)):
        if seq[i-1] > seq[i]:
            counter += 1
            if counter > 1:
                return False
    return True


class Tests(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(solve([10, 5, 7]))

    def test_example2(self):
        self.assertFalse(solve([10, 5, 1]))

