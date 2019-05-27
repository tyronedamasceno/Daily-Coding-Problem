"""
On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""

import unittest


def solve(bs):
    ans = 0
    for i, t1 in enumerate(bs):
        for t2 in bs[i+1:]:
            if abs(t1[0]-t2[0]) == abs(t1[1]-t2[1]):
                ans += 1
    return ans


class Tests(unittest.TestCase):

    def test_example(self):
        bishops = [(0,0), (1, 2), (2, 2), (4, 0)]
        self.assertEqual(solve(bishops), 2)

