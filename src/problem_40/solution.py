"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

import unittest

def solve(inp_list):
    bits_sum = [0]*32
    for x in inp_list:
        for i in range(32):
            if x & (1 << i):
                bits_sum[i] += 1
    bits_sum = [s%3 for s in bits_sum]
    ans = 0
    for i, s in enumerate(bits_sum):
        if s:
            ans += 2**i
    return ans

class Tests(unittest.TestCase):
    def test_example(self):
        inp = [6, 1, 3, 3, 3, 6, 6]
        self.assertEqual(solve(inp), 1)
    
    def test_example2(self):
        inp = [13, 19, 13, 13]
        self.assertEqual(solve(inp), 19)
