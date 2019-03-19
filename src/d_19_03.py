"""
Problem from day 19/03/2019

Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import unittest


def solve(inp_list, k):
    if len(inp_list) < 2:
        return False

    inp_dict = {}
    for x in inp_list:
        inp_dict[x] = inp_dict.get(x, 0) + 1
    for x in inp_list:
        inp_dict[x] -= 1
        target = k - x
        if inp_dict.get(target):
            return True
        inp_dict[x] += 1
    return False


class Tests(unittest.TestCase):
    def test_example(self):
        ans = solve([10, 15, 3, 7], 17)
        self.assertTrue(ans)

    def test_cant_use_the_same_element_twice(self):
        """In this test it should return false because it should not use two \
            times the same element. In the example, k=6 returns False
        """
        ans = solve([10, 15, 3, 7], 6)
        self.assertFalse(ans)

    def test_using_empty_or_unitary_list(self):
        ans1 = solve([], 10)
        ans2 = solve([1], 2)
        self.assertFalse(ans1)
        self.assertFalse(ans2)
