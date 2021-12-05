import numpy as np

# READ DATA
input = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/05.txt', 'r')
input = [x.strip().split(' -> ') for x in input.readlines()]
input = [[(el[0].split(',')), el[1].split(',')] for el in input]
input = [[[int(x[0][0]), int(x[0][1])], [int(x[1][0]), int(x[1][1])]] for x in input]

input_test = np.array([[[0,9],[5,9]],[[8,0],[0,8]],[[9,4], [3,4]],[[2,2], [2,1]],[[7,0], [7,4]],[[6,4], [2,0]],[[0,9], [2,9]],[[3,4], [1,4]],[[0,0], [8,8]],[[5,5], [8,2]]])

# DAY 1 PUZZLE 1

# Determine min and max of the board
min_X = min([min(x[0][0], x[1][0]) for x in input])
min_Y = min([min(x[0][1], x[1][1]) for x in input])
max_X = max([max(x[0][0], x[1][0]) for x in input])
max_Y = max([max(x[0][1], x[1][1]) for x in input])

# Configure initial board
board = np.zeros((max_X + 1, max_Y + 1))

# Get only vertical and horizontal
hor_and_vert = [el for el in input if ((el[0][0] ==  el[1][0]) or (el[0][1] ==  el[1][1]))]

for el in hor_and_vert:
    X1 = el[0][0]
    Y1 = el[0][1]
    X2 = el[1][0]
    Y2 = el[1][1]
    if(X1 == X2):
        if(Y2 > Y1):
            for y in range(Y1, Y2 + 1):
                board[X1][y] += 1
        if(Y1 > Y2):
            for y in range(Y2, Y1 + 1):
                board[X1][y] += 1
    if(Y1 == Y2):
        if(X2 > X1):
            for x in range(X1, X2 + 1):
                board[x][Y1] += 1
        if(X1 > X2):
            for x in range(X2, X1 + 1):
                board[x][Y1] += 1

res1 = len([el for el in board.flatten() if el > 1])
print('DAY 5 PUZZLE 1: %d' % (res1))


# DAY 1 PUZZLE 2
# Determine min and max of the board
min_X = min([min(x[0][0], x[1][0]) for x in input])
min_Y = min([min(x[0][1], x[1][1]) for x in input])
max_X = max([max(x[0][0], x[1][0]) for x in input])
max_Y = max([max(x[0][1], x[1][1]) for x in input])

# Configure initial board
board = np.zeros((max_X + 1, max_Y + 1))

# Get only vertical and horizontal
hor_and_vert_diag = [el for el in input if ((el[0][0] ==  el[1][0]) or (el[0][1] ==  el[1][1]) or (abs(el[0][0] - el[1][0]) ==  abs(el[0][1] - el[1][1])))]

for el in hor_and_vert_diag:
    X1 = el[0][0]
    Y1 = el[0][1]
    X2 = el[1][0]
    Y2 = el[1][1]
    if(X1 == X2):
        if(Y2 > Y1):
            for y in range(Y1, Y2 + 1):
                board[X1][y] += 1
        if(Y1 > Y2):
            for y in range(Y2, Y1 + 1):
                board[X1][y] += 1
    elif(Y1 == Y2):
        if(X2 > X1):
            for x in range(X1, X2 + 1):
                board[x][Y1] += 1
        if(X1 > X2):
            for x in range(X2, X1 + 1):
                board[x][Y1] += 1
    else:
        if(X2 > X1):
            for x in range(X1, X2 + 1):
                if(Y2 > Y1):
                    y = Y1 + (x - X1)
                    board[x][y] += 1
                if(Y1 > Y2):
                    y = Y1 - (x - X1)
                    board[x][y] += 1
        if(X1 > X2):
            for x in range(X2, X1 + 1):
                if(Y2 > Y1):
                    y = Y1 + (X1 - x)
                    board[x][y] += 1
                if(Y1 > Y2):
                    y = Y1 - (X1 - x)
                    board[x][y] += 1
                    
res2 = len([el for el in board.flatten() if el > 1])
print('DAY 5 PUZZLE 2: %d' % (res2))