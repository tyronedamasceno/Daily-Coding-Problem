"""
The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


import unittest
import string

def solve(s1, s2):
    dp = {}
    def solve_helper(n, m):
        if dp.get((n, m)):
            return dp.get((n, m))
        if n == 0:
            dp[(n, m)] = m
            return m
        if m == 0:
            dp[(n, m)] = n
            return n
        if s1[n-1] == s2[m-1]:
            dp[(n, m)] = solve_helper(n-1, m-1)
            return dp[(n, m)]
        dp[(n, m)] = 1 + min(
            solve_helper(n-1, m-1),
            solve_helper(n, m-1),
            solve_helper(n-1, m)
        )
        return dp[(n, m)]
    return solve_helper(len(s1), len(s2))


class Tests(unittest.TestCase):
    def test_example1(self):
        ans = solve('kitten', 'sitting')
        self.assertEqual(ans, 3)

    def test_asciiletters(self):
        ans = solve(string.ascii_lowercase, string.ascii_lowercase[::-1])
        self.assertEqual(ans, 26)

    def test_very_large_input(self):
        ans = solve('a'*500, 'b'*500)
        self.assertEqual(ans, 500)
