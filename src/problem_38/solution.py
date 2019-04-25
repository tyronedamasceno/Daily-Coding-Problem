"""
You have an N by N board. Write a function that, given N, returns the number of
possible arrangements of the board where N queens can be placed on the board
without threatening each other, i.e. no two queens share the same row, column,
or diagonal.
"""


import unittest


class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(1), 1)
    
    def test_two(self):
        self.assertEqual(solve(2), 0)
    
    def test_three(self):
        self.assertEqual(solve(3), 0)

    def test_four(self):
        self.assertEqual(solve(4), 2)

    def test_8_queens(self):
        self.assertEqual(solve(8), 92)
