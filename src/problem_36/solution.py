"""
Given the root to a binary search tree, find the second largest node in the tree.
"""

"""
My solution is quite simple:
The second largest node is the larger between the largest node's parent and its left subtree largest.

The solution time complexity is O(logn)
"""

import unittest


class Tests(unittest.TestCase):
    def test_example(self):
        pass
