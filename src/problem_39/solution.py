"""
Conway's Game of Life takes place on an infinite two-dimensional board of
square cells. Each cell is either dead or alive, and at each tick, the
following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or
diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a
starting list of live cell coordinates and the number of steps it should run
for. Once initialized, it should print out the board state at each step. Since
it's an infinite board, print out only the relevant coordinates, i.e. from the
top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

import os
from time import sleep
from copy import deepcopy
import random
import unittest


def run_game(coord_list, cycles=10, board_size=10):

    board = [['.']*board_size for i in range(board_size)]

    def print_board(gen):
        # os.system('clear')
        print(f'#{gen} generation')
        print()
        for row in board: 
            for cell in row: 
                print(cell, end='') 
            print()
        print('\n')

    for x, y in coord_list:
        board[x][y] = '*'
    new_board = deepcopy(board)
    
    sides = (-1, 0, -1)
    def count_alive_neighborhoods(x, y):
        counter = 0
        for i in sides:
            for j in sides:
                if (i or j) and (x+i) in range(board_size) and (y+j) in range(board_size) and board[x+i][y+j] == '*':
                    counter += 1
        return counter


    cont = 0
    while cont < cycles:
        cont += 1
        print_board(cont)
        sleep(1)
        for i in range(board_size):
            for j in range(board_size):
                alive_neighborhoods = count_alive_neighborhoods(i, j)
                if alive_neighborhoods:
                    print(f'({i},{j}) :: {alive_neighborhoods}')
                if board[i][j] == '*':
                    if alive_neighborhoods < 2 or alive_neighborhoods > 3:
                        new_board[i][j] = '.'
                else:
                    if alive_neighborhoods == 3:
                        new_board[i][j] = '*'
        board = deepcopy(new_board)

c = [(1, 1), (1, 2), (1, 3), (1, 5), (2, 1), (3, 4), (3, 5), (4, 2), (4, 3), (4, 5), (5, 1), (5, 3), (5, 5)]
run_game(c)