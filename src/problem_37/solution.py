"""
The power set of a set is the set of all its subsets. Write a function that,
given a set, generates its power set.

For example, given the set {1, 2, 3], it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""


import unittest


def powerset(base):
    ans = [[]]
    for x in base:
        to_add = [subans + [x] for subans in ans]
        ans.extend(to_add)
    return ans


class Tests(unittest.TestCase):
    def test_example(self):
        given = [1, 2, 3]
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(sorted(powerset(given)), sorted(expected))
