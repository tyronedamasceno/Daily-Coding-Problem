"""
Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:

2
1.5
2
3.5
2
2
2
"""

import unittest
import bisect

def solve(stream):
    ans = []
    helper = []
    for x in stream:
        bisect.insort(helper, x)
        h_sz = len(helper)
        if h_sz % 2 != 0:
            val = helper[h_sz//2]
            ans.append(val)
        else:
            val = helper[h_sz//2] + helper[(h_sz//2) - 1]
            ans.append(val/2)
    return ans


class Tests(unittest.TestCase):
    def test_example1(self):
        stream = [2, 1, 5, 7, 2, 0, 5]
        expected = [2, 1.5, 2, 3.5, 2, 2, 2]
        ans = solve(stream)
        for i, x in enumerate(ans):
            self.assertEqual(expected[i], x)
