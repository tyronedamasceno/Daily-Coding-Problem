"""
Implement locking in a binary tree. A binary tree node can be locked or
unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

- is_locked, which returns whether the node is locked
- lock, which attempts to lock the node. If it cannot be locked, then it should
  return false. Otherwise, it should lock it and return true.
- unlock, which unlocks the node. If it cannot be unlocked, then it should
  return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you
would like. You may assume the class is used in a single-threaded program,
so there is no need for actual locks or mutexes. Each method should run in
O(h), where h is the height of the tree.
"""

import unittest

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.locked = False
        self.locked_descendants = 0
    
    def is_locked(self):
        return self.locked

    def _is_lockable(self):
        if self.locked_descendants:
            return False

        parent = self.parent
        while parent:
            if parent.is_locked():
                return False
            parent = parent.parent
        self.locked = True
        return True

    def lock(self):
        if self._is_lockable():
            if not self.is_locked():
                self.locked = True
                parent = self.parent
                while parent:
                    parent.locked_descendants += 1
                    parent = parent.parent
            return True
        else:
            return False

    def unlock(self):
        if self._is_lockable():
            if self.is_locked():
                self.locked = False
                parent = self.parent
                while parent:
                    parent.locked_descendants -= 1
                    parent = parent.parent
            return True
        else:
            return False


class Tests(unittest.TestCase):
    def test_example(self):
        pass
