"""
The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


import unittest

def solve(s1, s2):
    def solve_helper(n, m):
        if n == 0:
            return m
        if m == 0:
            return n
        if s1[n-1] == s2[m-1]:
            return solve_helper(n-1, m-1)
        return 1 + min(
            solve_helper(n-1, m-1),
            solve_helper(n, m-1),
            solve_helper(n-1, m)
        )
    return solve_helper(len(s1), len(s2))


class Tests(unittest.TestCase):
    def test_example1(self):
        ans = solve('kitten', 'sitting')
        self.assertEqual(ans, 3)
