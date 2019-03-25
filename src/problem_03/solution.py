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

    def test_hard(self):
        super_left_tree = (
            Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8,
            Node(9, Node(10, Node(11, Node(12, Node(13, Node(14, Node(15,
            Node(16, Node(17, Node(19, Node(18, Node(20, Node(21, Node(22,
            Node(23, Node(24, Node(25, Node(26, Node(27, Node(28, Node(29,
            Node(30, Node(31, Node(32, Node(33, Node(34, Node(35, Node(36,
            Node(37, Node(38, Node(39, Node(40, Node(41, Node(42, Node(43,
            Node(44, Node(45, Node(46, Node(47, Node(48,
            Node(49)))))))))))))))))))))))))))))))))))))))))))))))))
        )
        str_tree = serialize(super_left_tree)
        first_null = str_tree.find('@')
        for x in range(1, 50):
            self.assertIn(str(x), str_tree[:first_null])