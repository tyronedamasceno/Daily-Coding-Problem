"""
Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

import unittest


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
