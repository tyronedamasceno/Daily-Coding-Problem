"""
Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


"""
My solution time complexity is O(n) in both sulutions, where n is the input 
list length.
But the solution bonus 'in one pass' has a better constant, because it 
just iterate once over the input.
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


def solve_in_one_pass(inp_list, k):
    if len(inp_list) < 2:
        return False
    
    inp_set = set()
    for x in inp_list:
        target = k - x
        if target in inp_set:
            return True
        inp_set.add(x)
    return False


class Tests(unittest.TestCase):
    def test_example(self):
        ans = solve_in_one_pass([10, 15, 3, 7], 17)
        # ans = solve([10, 15, 3, 7], 17)
        self.assertTrue(ans)

    def test_cant_use_the_same_element_twice(self):
        """In this test it should return false because it should not use two \
            times the same element. In the example, k=6 returns False
        """
        ans = solve_in_one_pass([10, 15, 3, 7], 6)
        # ans = solve([10, 15, 3, 7], 6)
        self.assertFalse(ans)

    def test_using_empty_or_unitary_list(self):
        ans1 = solve_in_one_pass([], 10)
        ans2 = solve_in_one_pass([1], 2)
        # ans1 = solve([], 10)
        # ans2 = solve([1], 2)
        self.assertFalse(ans1)
        self.assertFalse(ans2)

    def test_with_large_input(self):
        """In this test it use a really large input (n=10**4) made only by \
            even numbers    
        """
        with open("large_input_evens.txt") as f:
            l = [int(x) for x in f.readline().split(",")]
        ans_odd = solve_in_one_pass(l, 1001)
        ans_even = solve_in_one_pass(l, l[0] + l[-1])
        # ans_odd = solve(l, 1001)
        # ans_even = solve(l, l[0] + l[-1]
        self.assertFalse(ans_odd)
        self.assertTrue(ans_even)

    def test_with_negative_numbers_on_input(self):
        l = [5, -2, 8, 3, 11, -7]
        ans_ok1 = solve_in_one_pass(l, -9)
        ans_ok2 = solve_in_one_pass(l, -4)
        # ans_ok1 = solve(l, -9)
        # ans_ok2 = solve(l, -4)
        self.assertTrue(ans_ok1)
        self.assertTrue(ans_ok2)
