import numpy as np

# READ DATA
input = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/09.txt', 'r')
input = [x.strip() for x in input.readlines()]
input = [list(el) for el in input]
input = np.array([list(map(int, x)) for x in (el for el in input)])

input_test = ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']
input_test = [list(el) for el in input_test]
input_test = np.array([list(map(int, x)) for x in (el for el in input_test)])

INPUT = input

# DAY 8 PUZZLE 1

res = 0

# Recorriendo interior
len_x = INPUT.shape[0]
len_y = INPUT.shape[1]
for x in range(1, len_x - 1):
    for y in range(1, len_y - 1):
        if(INPUT[x][y] < min(INPUT[x - 1][y], INPUT[x][y - 1], INPUT[x][y + 1], INPUT[x + 1][y])): res += INPUT[x][y] + 1

# Recorriendo esquinas
if(INPUT[0][0] < min(INPUT[0][1], INPUT[1][0])): res += INPUT[0][0] + 1
if(INPUT[0][len_y - 1] < min(INPUT[0][len_y - 2], INPUT[1][len_y - 1])): res += INPUT[0][len_y - 1] + 1
if(INPUT[len_x - 1][0] < min(INPUT[len_x - 2][0], INPUT[len_x - 1][1])): res += INPUT[len_x - 1][0] + 1
if(INPUT[len_x - 1][len_y - 1] < min(INPUT[len_x - 2][len_y - 1], INPUT[len_x - 1][len_y - 2])): res += INPUT[len_x - 1][len_y - 1] + 1

# Recorriendo aristas
for x in range(1, len_x - 1):
    if(INPUT[x][0] < min(INPUT[x - 1][0], INPUT[x][1], INPUT[x + 1][0])): res += INPUT[x][0] + 1
    if(INPUT[x][len_y - 1] < min(INPUT[x - 1][len_y - 1], INPUT[x][len_y - 2], INPUT[x + 1][len_y - 1])): res += INPUT[x][len_y - 1] + 1

for y in range(1, len_y - 1):
    if(INPUT[0][y] < min(INPUT[0][y - 1], INPUT[1][y], INPUT[0][y + 1])): res += INPUT[0][y] + 1
    if(INPUT[len_x - 1][y] < min(INPUT[len_x - 1][y - 1], INPUT[len_x - 2][y], INPUT[len_x - 1][y + 1])): res += INPUT[len_x - 1][y] + 1

res1 = res
print('DAY 9 PUZZLE 1: %d' % (res1))


# DAY 8 PUZZLE 2

res = np.array([])

# Recorriendo interior
len_x = INPUT.shape[0]
len_y = INPUT.shape[1]
for x in range(1, len_x - 1):
    for y in range(1, len_y - 1):
        if(INPUT[x][y] < min(INPUT[x - 1][y], INPUT[x][y - 1], INPUT[x][y + 1], INPUT[x + 1][y])): 
            if (res.size == 0): 
                res = np.vstack(([x, y])).transpose()
            else: 
                res = np.vstack((res, [x, y]))

# Recorriendo esquinas
if(INPUT[0][0] < min(INPUT[0][1], INPUT[1][0])): res = np.vstack((res, [0, 0]))
if(INPUT[0][len_y - 1] < min(INPUT[0][len_y - 2], INPUT[1][len_y - 1])): res = np.vstack((res, [0, len_y - 1]))
if(INPUT[len_x - 1][0] < min(INPUT[len_x - 2][0], INPUT[len_x - 1][1])): res = np.vstack((res, [len_x - 1, 0]))
if(INPUT[len_x - 1][len_y - 1] < min(INPUT[len_x - 2][len_y - 1], INPUT[len_x - 1][len_y - 2])): res = np.vstack((res, [len_x - 1, len_y - 1]))

# Recorriendo aristas
for x in range(1, len_x - 1):
    if(INPUT[x][0] < min(INPUT[x - 1][0], INPUT[x][1], INPUT[x + 1][0])): res = np.vstack((res, [x, 0]))
    if(INPUT[x][len_y - 1] < min(INPUT[x - 1][len_y - 1], INPUT[x][len_y - 2], INPUT[x + 1][len_y - 1])): res = np.vstack((res, [x, len_y - 1]))

for y in range(1, len_y - 1):
    if(INPUT[0][y] < min(INPUT[0][y - 1], INPUT[1][y], INPUT[0][y + 1])): res = np.vstack((res, [0, y]))
    if(INPUT[len_x - 1][y] < min(INPUT[len_x - 1][y - 1], INPUT[len_x - 2][y], INPUT[len_x - 1][y + 1])): res = np.vstack((res, [len_x - 1, y]))

def neighbours(matrix, x, y, elements):

    if([x, y] not in elements): elements.append([x, y])

    len_x = matrix.shape[0]
    len_y = matrix.shape[1]

    if((x - 1) >= 0):
        if([x - 1, y] not in elements):
            if(matrix[x - 1][y] != 9): 
                elements = neighbours(matrix, x - 1, y, elements)

    if((y - 1) >= 0):
        if([x, y - 1] not in elements):
            if(matrix[x][y - 1] != 9): 
                elements = neighbours(matrix, x, y - 1, elements)

    if((x + 1) < len_x):
        if([x + 1, y] not in elements):
            if(matrix[x + 1][y] != 9): 
                elements = neighbours(matrix, x + 1, y, elements) 

    if((y + 1) < len_y):
        if([x, y + 1] not in elements):
            if(matrix[x][y + 1] != 9): 
                elements = neighbours(matrix, x, y + 1, elements)
    
    return elements

len_of_basin = []
for x, y in res:
    elements = [[x, y]]
    elements = neighbours(INPUT, x, y, elements)
    len_of_basin.append(len(elements))

len_of_basin.sort(reverse = True)

res2 = len_of_basin[0] * len_of_basin[1] * len_of_basin[2]
print('DAY 9 PUZZLE 2: %d' % (res2))