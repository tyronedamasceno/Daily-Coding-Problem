"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

import unittest

"""
This solution works but it's has exponential time complexity
"""
def solve(inp_list):
    def solve_inner(inp_list, pos, sum):
        if pos >= len(inp_list):
            return sum
        x = sum + inp_list[pos]
        return max(
            solve_inner(inp_list, pos+2, x),
            solve_inner(inp_list, pos+1, sum)
        )
    return solve_inner(inp_list, 0, 0)


class Tests(unittest.TestCase):
    def test_example_1(self):
        ans = solve([2, 4, 6, 2, 5])
        self.assertEqual(ans, 13)
    
    def test_example_2(self):
        ans = solve([5, 1, 1, 5])
        self.assertEqual(ans, 10)

    def test_with_negative_numbers(self):
        ans = solve([-2, 0, -7])
        self.assertEqual(ans, 0)
    
    def test_empty_list(self):
        ans = solve([])
        self.assertEqual(ans, 0)

    def test_with_medium_input(self):
        l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        ans = solve(l)
        self.assertEqual(ans, 100)

    def test_with_large_input(self):
        l = [x for x in range(100)]
        ans = solve(l)
        self.assertEqual(ans, 2500)
