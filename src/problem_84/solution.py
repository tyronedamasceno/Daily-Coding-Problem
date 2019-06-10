"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

import unittest
import queue

def count_islands(matrix):
    visited = {}
    ans = 0
    def visit_neighborhoods(x, y):
        q = queue.Queue()
        q.put((x, y))
        while not q.empty():
            i, j = q.get()
            visited[(i, j)] = True
            if i > 0 and not visited.get((i-1, j)) and matrix[i-1][j]:
                q.put((i-1, j))
            if j > 0 and not visited.get((i, j-1)) and matrix[i][j-1]:
                q.put((i, j-1))
            if i < len(matrix)-1 and not visited.get((i+1, j)) and matrix[i+1][j]:
                q.put((i+1, j))
            if j < len(matrix[i])-1 and not visited.get((i, j+1)) and matrix[i][j+1]:
                q.put((i, j+1))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j]:
                continue
            if not visited.get((i, j)):
                visited[(i, j)] = True
                ans += 1
                visit_neighborhoods(i, j)


    return ans

class Tests(unittest.TestCase):
    def test_example(self):
        matrix = [
            [1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1]
        ]
        islands = count_islands(matrix)
        self.assertEqual(islands, 4)

