import numpy as np

# READ DATA
input = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/11.txt', 'r')
input = [x.strip() for x in input.readlines()]
input = [list(el) for el in input]
input = np.array([list(map(int, x)) for x in (el for el in input)])

input_test = ['5483143223', '2745854711', '5264556173', '6141336146', '6357385478', '4167524645', '2176841721', '6882881134', '4846848554', '5283751526']
input_test = [list(el) for el in input_test]
input_test = np.array([list(map(int, x)) for x in (el for el in input_test)])

INPUT = input_test

# DAY 11 PUZZLE 1

flashes = 0

print('Before any steps:')
print(INPUT)
print()

for step in range(1, 201):

    temp = np.zeros(INPUT.shape)

    print('After step %d:' % (step))

    INPUT = INPUT + 1

    len_x = INPUT.shape[0]
    len_y = INPUT.shape[1]

    for aux in range(20):
        for i in range(0, len_x):
            for j in range(0, len_y):
                if(INPUT[i][j] > 9 and temp[i][j] == 0):
                    temp[i][j] = 1
                    flashes += 1
                    if(i == 0 and j == 0):
                        INPUT[1][0] += 1
                        INPUT[1][1] += 1
                        INPUT[0][1] += 1
                    elif(i == 0 and j == (len_y - 1)):
                        INPUT[0][len_y - 2] += 1
                        INPUT[1][len_y - 2] += 1
                        INPUT[1][len_y - 1] += 1
                    elif(i == (len_x - 1) and j == 0):
                        INPUT[len_x - 2][0] += 1
                        INPUT[len_x - 2][1] += 1
                        INPUT[len_x - 1][1] += 1
                    elif(i == (len_x - 1) and j == (len_y - 1)):
                        INPUT[len_x - 2][len_y - 1] += 1
                        INPUT[len_x - 2][len_y - 2] += 1
                        INPUT[len_x - 1][len_y - 2] += 1
                    elif(i == 0 and j > 0 and j < (len_y - 1)):
                        INPUT[0][j - 1] += 1
                        INPUT[1][j - 1] += 1
                        INPUT[1][j] += 1 
                        INPUT[1][j + 1] += 1 
                        INPUT[0][j + 1] += 1 
                    elif(i == (len_x - 1) and j > 0 and j < (len_y - 1)):
                        INPUT[len_x - 1][j - 1] += 1
                        INPUT[len_x - 2][j - 1] += 1
                        INPUT[len_x - 2][j] += 1 
                        INPUT[len_x - 2][j + 1] += 1 
                        INPUT[len_x - 1][j + 1] += 1 
                    elif(i > 0 and i < (len_x - 1) and j == 0):
                        INPUT[i - 1][0] += 1
                        INPUT[i - 1][1] += 1
                        INPUT[i][1] += 1 
                        INPUT[i + 1][1] += 1 
                        INPUT[i + 1][0] += 1 
                    elif(i > 0 and i < (len_x - 1) and j == (len_y - 1)):
                        INPUT[i - 1][len_y - 1] += 1
                        INPUT[i - 1][len_y - 2] += 1
                        INPUT[i][len_y - 2] += 1 
                        INPUT[i + 1][len_y - 2] += 1 
                        INPUT[i + 1][len_y - 1] += 1 
                    else:
                        INPUT[i - 1][j - 1] += 1
                        INPUT[i][j - 1] += 1
                        INPUT[i + 1][j - 1] += 1
                        INPUT[i - 1][j] += 1
                        INPUT[i + 1][j] += 1
                        INPUT[i - 1][j + 1] += 1
                        INPUT[i][j + 1] += 1
                        INPUT[i + 1][j + 1] += 1
        
    for i in range(0, len_x):
        for j in range(0, len_y):
            if(INPUT[i][j] > 9): INPUT[i][j] = 0
    
    print(INPUT)
    print()

res1 = flashes
print('DAY 10 PUZZLE 1: %d' % (res1))


# DAY 11 PUZZLE 2

INPUT = input

flashes = 0

print('Before any steps:')
print(INPUT)
print()

for step in range(1, 2000):

    temp = np.zeros(INPUT.shape)

    print('After step %d:' % (step))

    INPUT = INPUT + 1

    len_x = INPUT.shape[0]
    len_y = INPUT.shape[1]

    for aux in range(20):
        for i in range(0, len_x):
            for j in range(0, len_y):
                if(INPUT[i][j] > 9 and temp[i][j] == 0):
                    temp[i][j] = 1
                    flashes += 1
                    if(i == 0 and j == 0):
                        INPUT[1][0] += 1
                        INPUT[1][1] += 1
                        INPUT[0][1] += 1
                    elif(i == 0 and j == (len_y - 1)):
                        INPUT[0][len_y - 2] += 1
                        INPUT[1][len_y - 2] += 1
                        INPUT[1][len_y - 1] += 1
                    elif(i == (len_x - 1) and j == 0):
                        INPUT[len_x - 2][0] += 1
                        INPUT[len_x - 2][1] += 1
                        INPUT[len_x - 1][1] += 1
                    elif(i == (len_x - 1) and j == (len_y - 1)):
                        INPUT[len_x - 2][len_y - 1] += 1
                        INPUT[len_x - 2][len_y - 2] += 1
                        INPUT[len_x - 1][len_y - 2] += 1
                    elif(i == 0 and j > 0 and j < (len_y - 1)):
                        INPUT[0][j - 1] += 1
                        INPUT[1][j - 1] += 1
                        INPUT[1][j] += 1 
                        INPUT[1][j + 1] += 1 
                        INPUT[0][j + 1] += 1 
                    elif(i == (len_x - 1) and j > 0 and j < (len_y - 1)):
                        INPUT[len_x - 1][j - 1] += 1
                        INPUT[len_x - 2][j - 1] += 1
                        INPUT[len_x - 2][j] += 1 
                        INPUT[len_x - 2][j + 1] += 1 
                        INPUT[len_x - 1][j + 1] += 1 
                    elif(i > 0 and i < (len_x - 1) and j == 0):
                        INPUT[i - 1][0] += 1
                        INPUT[i - 1][1] += 1
                        INPUT[i][1] += 1 
                        INPUT[i + 1][1] += 1 
                        INPUT[i + 1][0] += 1 
                    elif(i > 0 and i < (len_x - 1) and j == (len_y - 1)):
                        INPUT[i - 1][len_y - 1] += 1
                        INPUT[i - 1][len_y - 2] += 1
                        INPUT[i][len_y - 2] += 1 
                        INPUT[i + 1][len_y - 2] += 1 
                        INPUT[i + 1][len_y - 1] += 1 
                    else:
                        INPUT[i - 1][j - 1] += 1
                        INPUT[i][j - 1] += 1
                        INPUT[i + 1][j - 1] += 1
                        INPUT[i - 1][j] += 1
                        INPUT[i + 1][j] += 1
                        INPUT[i - 1][j + 1] += 1
                        INPUT[i][j + 1] += 1
                        INPUT[i + 1][j + 1] += 1
        
    for i in range(0, len_x):
        for j in range(0, len_y):
            if(INPUT[i][j] > 9): INPUT[i][j] = 0
    
    print(INPUT)
    print()

    if(np.sum(INPUT) == 0): 
        res2 = step
        break

print('DAY 10 PUZZLE 2: %d' % (res2))