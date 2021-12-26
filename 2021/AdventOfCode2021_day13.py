import numpy as np
import math
np.set_printoptions(threshold=np.inf)

import matplotlib.pyplot as plt

# READ DATA
INPUT = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/13.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
input_coordinates = INPUT[0:INPUT.index('')]
input_coordinates = [el.split(',') for el in input_coordinates]
input_coordinates = [[int(el[0]), int(el[1])] for el in input_coordinates]
input_folds = INPUT[INPUT.index('')+1:]

input_test_coordinates = [[6,10],[0,14],[9,10],[0,3],[10,4],[4,11],[6,0],[6,12],[4,1],[0,13],[10,12],[3,4],[3,0],[8,4],[1,10],[2,14],[8,10],[9,0]]
input_test_folds = ['fold along y=7', 'fold along x=5']

INPUT_COORDINATES = input_coordinates
INPUT_FOLDS = input_folds

# DAY 13 PUZZLE 1
len_x = max([el[0] for el in INPUT_COORDINATES]) + 1
len_y = max([el[1] for el in INPUT_COORDINATES]) + 1

board = np.zeros((len_x, len_y), str)
board[board == ''] = '.'
for el in INPUT_COORDINATES: board[el[0]][el[1]] = '#'

for el in INPUT_FOLDS:
    len_x = board.shape[0]
    len_y = board.shape[1]
    temp = el.split('=')
    axis = temp[0][-1]
    value = temp[1]
    if(axis == 'x'):
        for i in range(len_x):
            for j in range(len_y):
                if(board[i][j] == '#' or board[len_x - 1 - i][j] == '#'): board[i][j] = '#'
        board = board[0:int(value), 0:len_y]
        res1 = np.count_nonzero(board == '#')
        break
    if(axis == 'y'):
        for i in range(len_x):
            for j in range(len_y):
                if(board[i][j] == '#' or board[i][len_y - 1 - j] == '#'): board[i][j] = '#'
        board = board[0:len_x, 0:int(value)]
        res1 = np.count_nonzero(board == '#')
        break

print('DAY 13 PUZZLE 1: %d' % (res1))

# DAY 13 PUZZLE 2
n_columns = max([el[0] for el in INPUT_COORDINATES]) + 1
n_rows = max([el[1] for el in INPUT_COORDINATES]) + 1

board = np.zeros((n_rows, n_columns))
for el in INPUT_COORDINATES: 
    board[el[1], el[0]] = 1

for el in INPUT_FOLDS:
    [n_rows, n_columns] = board.shape
    temp = el.split('=')
    axis = temp[0][-1]
    value = int(temp[1])
    if(axis == 'x'):
        for c in range(value):
            for r in range(n_rows):
                if (value + (value - c)) < n_columns:
                    board[r, c] = max(board[r, c], board[r, value + (value - c)])
        board = board[:, :value]
    if(axis == 'y'):
        for c in range(n_columns):
            for r in range(value):
                if(value + (value - r)) < n_rows:
                    board[r, c] = max(board[r, c], board[value + (value - r), c])
        board = board[:value, :]

plt.matshow(board)
plt.show()