import numpy as np

# READ DATA
INPUT = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/04.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

# LISTA DE ELEMENTOS DEL BINGO
input_list = [int(x) for x in INPUT[0].split(',')]
input_list_test = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

# LISTA DE CARTONES DE BINGO
boards_test = np.array([[
    [22, 13, 17, 11, 0], 
    [8, 2, 23, 4, 24], 
    [21, 9, 14, 16, 7], 
    [6, 10, 3, 18, 5], 
    [1, 12, 20, 15, 19]],
    [[3, 15, 0, 2, 22],
    [9, 18, 13, 17, 5],
    [19, 8, 7, 25, 23],
    [20, 11, 10, 24, 4],
    [14, 21, 16, 12, 6]],
    [[14, 21, 17, 24, 4],
    [10, 16, 15, 9, 19],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, 3, 7]]])
boards = [INPUT[2:][n:n+5] for n in range(0, len(INPUT[2:]), 6)]
for i in range(0, len(boards)):
    for j in range(0, len(boards[0])):
        boards[i][j] = [int(x) for x in boards[i][j].split()]
boards = np.array(boards)

# DAY 4 PUZZLE 1
results_test = np.zeros((boards_test.shape))
results = np.zeros((boards.shape))
    # In boards and results:
    #   index 0: board
    #   index 1: row
    #   index 2: column
solved = False
for el in input_list:
    res = np.array(np.where(boards == el)).transpose()
    for (i, j, k) in res: results[i][j][k] = 1
    for i in range(len(results)):
        sum_rows = np.sum(results[i], axis = 0)
        sum_columns = np.sum(results[i], axis = 1)
        if(np.any(sum_rows == 5) or np.any(sum_columns == 5)): 
            solved = True
            break
    if(solved): break

sum = 0
for j in range(len(results[i])):
    for k in range(len(results[i][j])):
        if(results[i][j][k] == 0): sum += boards[i][j][k]

res1 = sum * el
print('DAY 4 PUZZLE 1: %d' % (res1))


# DAY 4 PUZZLE 2
results = np.zeros((boards.shape))
    # In boards and results:
    #   index 0: board
    #   index 1: row
    #   index 2: column
solved = np.zeros(boards.shape[0])
for el in input_list:
    res = np.array(np.where(boards == el)).transpose()
    for (i, j, k) in res: results[i][j][k] = 1
    for i in range(len(results)):
        sum_rows = np.sum(results[i], axis = 0)
        sum_columns = np.sum(results[i], axis = 1)
        if(solved[i] == 0 and (np.any(sum_rows == 5) or np.any(sum_columns == 5))): 
            solved[i] = 1
            if(np.sum(solved) == 100): break
    if(np.sum(solved) == 100): break
                
sum = 0
for j in range(len(results[i])):
    for k in range(len(results[i][j])):
        if(results[i][j][k] == 0): sum += boards[i][j][k]
res2 = sum * el
print('DAY 4 PUZZLE 2: %d' % (res2))