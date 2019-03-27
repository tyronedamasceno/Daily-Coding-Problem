"""
A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

import unittest

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tests(unittest.TestCase):
    def test_example(self):
        tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
        ans = solve(tree)
        self.assertEqual(ans, 5)