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
    
    def is_leave(self):
        return self.left is None and self.right is None

total = 0
def solve(node):
    if node.is_leave():
        globals()['total'] += 1
        return True
    if not node.left is None and not node.right is None:
        unival_left = solve(node.left)
        unival_right = solve(node.right)
        if unival_left and unival_right and (
            node.value == node.left.value and node.value == node.right.value):
            globals()['total'] += 1
            return True
        return False
    elif not node.left is None:
        unival_left = solve(node.left)
        if unival_left and node.value == node.left.value:
            globals()['total'] += 1
            return True
    else:
        unival_right = solve(node.right)
        if unival_left and node.value == node.right.value:
            globals()['total'] += 1
            return True


class Tests(unittest.TestCase):
    def test_example(self):
        tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
        globals()['total'] = 0
        solve(tree)
        self.assertEqual(globals()['total'], 5)

    def test_one_single_node(self):
        tree = Node(1)
        globals()['total'] = 0
        solve(tree)
        self.assertEqual(globals()['total'], 1)

    def test_complete_tree(self):
        tree = Node(1, Node(1), Node(1))
        globals()['total'] = 0
        solve(tree)
        self.assertEqual(globals()['total'], 3)
    
    def test_complete_tree_with_distinct_nodes(self):
        tree = Node(1, Node(2), Node(3))
        globals()['total'] = 0
        solve(tree)
        self.assertEqual(globals()['total'], 2)