"""
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the
minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down,
and right. You cannot move through walls. You cannot wrap around the edges
of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
number of steps required to reach the end is 7, since we would need to go
through (1, 2) because there is a wall everywhere else on the second row.
"""

"""
Time complexity is O(n*m) and space complexity is O(n*m)
"""


import unittest
import queue

def solve(board, start, end):
    n = len(board)
    m = len(board[0])
    visited = {(x, y): False for x in range(n) for y in range(m)}
    visited[start] = True
    q = queue.Queue()
    q.put((*start, 0))
    while not q.empty():
        x, y, k = q.get()
        if (x, y) == end:
            return k
        visited[(x, y)] = True
        if x > 0 and not visited[(x-1, y)] and not board[x-1][y]:
            q.put((x-1, y, k+1))
        if y > 0 and not visited[(x, y-1)] and not board[x][y-1]:
            q.put((x, y-1, k+1))
        if x < n - 1 and not visited[(x+1, y)] and not board[x+1][y]:
            q.put((x+1, y, k+1))
        if y < m - 1 and not visited[(x, y+1)] and not board[x][y+1]:
            q.put((x, y+1, k+1))
    return None


class Tests(unittest.TestCase):
    def test_example(self):
        board = [
            [False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]
        ]
        start = (3, 0)
        end = (0, 0)
        ans = solve(board, start, end)
        self.assertEqual(ans, 7)

    def test_no_way(self):
        board = [
            [False, False, False, False],
            [True, True, True, True],
            [False, False, False, False],
            [False, False, False, False]
        ]
        start = (3, 0)
        end = (0, 0)
        ans = solve(board, start, end)
        self.assertEqual(ans, None)
