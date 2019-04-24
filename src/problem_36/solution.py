"""
Given the root to a binary search tree, find the second largest node in the tree.
"""

"""
My solution is quite simple:
The second largest node is the larger between the largest node's parent and its
left subtree largest.

The solution time complexity is O(logn)
"""

import unittest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leave(self):
        return not self.left and not self.right


def second_largest(root):
    if root.is_leave():
        return None
    elif not root.right:
        root = root.left
        while root.right:
            root = root.right
        return root.val
    else:
        ans = root.val
        root = root.right
        while root.right:
            ans = root.val
            root = root.right
        if root.is_leave():
            return ans
        root = root.left
        while root.right:
            root = root.right
        return root.val


class Tests(unittest.TestCase):
    def test_largest_with_no_children(self):
        BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14)))
        ans = second_largest(BST)
        self.assertEqual(ans, 10)

    def test_largest_with_left_children(self):
        BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
        ans = second_largest(BST)
        self.assertEqual(ans, 13)

    def test_root_with_no_right_subtree(self):
        BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))))
        ans = second_largest(BST)
        self.assertEqual(ans, 7)

    def test_tree_with_root_only(self):
        BST = Node(8)
        ans = second_largest(BST)
        self.assertIsNone(ans)
