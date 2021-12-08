import numpy as np
import math

# READ DATA
input = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/07.txt', 'r')
input = [x.strip().split(',') for x in input.readlines()][0]
input = [int(x) for x in input]

input_test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

INPUT = np.array(input)

# DAY 7 PUZZLE 1
median = np.median(INPUT)
fuel = 0
for el in INPUT:
    fuel += abs(median - el)
res1 = fuel
print('DAY 7 PUZZLE 1: %d' % (res1))


# DAY 7 PUZZLE 2
mean = int(math.floor(np.mean(INPUT)))
fuel = 0
for el in INPUT:
    res = abs(el - mean)
    for i in range(1, res + 1):
        fuel += i
res2 = fuel
print('DAY 7 PUZZLE 2: %d' % (res2))