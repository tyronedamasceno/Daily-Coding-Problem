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
    

def serialize(tree_root):
    nodes_list = perform_serialize(tree_root)
    return ' '.join(str(node_val) for node_val in nodes_list)


def perform_serialize(node):
    nodes_list = []
    if node:
        nodes_list.append(node.val)
        nodes_list.extend(perform_serialize(node.left))
        nodes_list.extend(perform_serialize(node.right))
    else:
        nodes_list.append('@')  # '@' means null
    return nodes_list


def deserialize(tree_str):
    tree_list = tree_str.split(' ')
    return perform_deserialize(tree_list)


def perform_deserialize(nodes_list):
    if len(nodes_list):
        value = nodes_list.pop(0)
        if value != '@':
            node = Node(value)
            node.left = perform_deserialize(nodes_list)
            node.right = perform_deserialize(nodes_list)
        else:
            node = Node(None)
    return node


class Tests(unittest.TestCase):
     def test_example(self):
         node = Node('root', Node('left', Node('left.left')), Node('right'))
         self.assertEqual(
             deserialize(serialize(node)).left.left.val, 'left.left'
         )

