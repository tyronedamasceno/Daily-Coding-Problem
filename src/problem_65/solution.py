"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12
"""

import unittest


def solve(matrix):
    heigth = len(matrix)
    width = len(matrix[0])
    direction, way = 'h', 1


class Tests(unittest.TestCase):
    def test_example(self):
        matrix = [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        output = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
        self.assertEqual(solve(matrix), output)

