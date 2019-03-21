"""
Problem from day 21/03/2019

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string
back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def serialize(node):
    left_son = ''
    right_son = ''
    if node.left:
        left_son = serialize(node.left)
    if node.right:
        right_son = serialize(node.right)
    if left_son == '' and right_son == '':
        return f'{node.val}'
    return f'{node.val}: ({left_son} - {right_son})'
    

def deserialize(node_str):
    pass


class Tests(unittest.TestCase):
     def test_example(self):
         node = Node('root', Node('left', Node('left.left')), Node('right'))
         self.assertEqual(
             deserialize(serialize(node)).left.left.val, 'left.left'
         )

