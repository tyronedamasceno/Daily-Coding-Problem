"""
Given a 2D matrix of characters and a target word, write a function that
returns whether the word can be found in the matrix by going left-to-right,
or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost
column. Similarly, given the target word 'MASS', you should return true,
since it's the last row.
"""

import unittest
from copy import deepcopy

def solve(matrix, word):
    transp = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transp[i][j] = matrix[j][i]
    for line in matrix:
        if word in ''.join(line):
            return True
    for line in transp:
        if word in ''.join(line):
            return True
    return False


class Tests(unittest.TestCase):
    def test_example1(self):
        matrix = [
            ['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S']
        ]
        self.assertTrue(solve(matrix, 'FOAM'))

    def test_example2(self):
        matrix = [
            ['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S']
        ]
        self.assertTrue(solve(matrix, 'MASS'))

