"""
Given a singly linked list and an integer k, remove the kth last element from
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

import unittest

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        while self:
            values.append(str(self.val))
            self = self.next
        return ' -> '.join(values)


def remove_k_last_from_list(head, k):
    p1 = head
    while k > 0:
        p1 = p1.next
        k -= 1
    
    while p1.next:
        head = head.next
        p1 = p1.next
    head.next = None


class Tests(unittest.TestCase):
    def test_example(self):
        head = Node(5, Node(3, Node(3, Node(1, Node(4)))))
        self.assertEqual(str(head), '5 -> 3 -> 3 -> 1 -> 4')
        remove_k_last_from_list(head, 3)
        self.assertEqual(str(head), '5 -> 3')
