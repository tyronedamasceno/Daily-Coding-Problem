"""
Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

"""
Solution time complexity is O(nlogn) due to sorting the input list.
"""

import unittest

def solve(inp_list=None):
    if not inp_list:
        return 0
    inp_list = sorted(inp_list)
    cur = inp_list[0]
    ans = 1
    cur_ans = 1
    for tup in inp_list[1:]:
        if cur[1] > tup[0]:  # Begin of next class is before the end of the current class
            cur_ans += 1
        else:
            cur = tup
            cur_ans = 1
        ans = max(ans, cur_ans)
    return ans


class Tests(unittest.TestCase):
    def test_example(self):
        x = [(30, 75), (0, 50), (60, 150)]
        self.assertEqual(solve(x), 2)

    def test_empty_lists(self):
        self.assertEqual(solve(), 0)
        self.assertEqual(solve([]), 0)

    def test_two(self):
        x = [(30, 75), (0, 50), (60, 150), (10, 87), (100, 120), (40, 80), (150, 200)]
        self.assertEqual(solve(x), 4)
