"""
Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

import unittest


def solve(inp):
    stack = []
    opens = ('(', '[', '{')
    closes = (')', ']', '}')
    for b in inp:
        if b in opens:
            stack.append(b)
        elif b in closes:
            if not stack:
                return False
            if not opens.index(stack.pop()) == closes.index(b):
                return False
        else:
            return False
    return not stack


class Tests(unittest.TestCase):
    def test_example_1(self):
        inp = '([])[]({})'
        self.assertTrue(solve(inp))

    def test_example_2(self):
        inp = '([)]'
        self.assertFalse(solve(inp))

    def test_example_3(self):
        inp = '((()'
        self.assertFalse(solve(inp))
