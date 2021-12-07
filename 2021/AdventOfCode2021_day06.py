import numpy as np
from numpy.core.numeric import count_nonzero

# READ DATA
input = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/06.txt', 'r')
input = [x.strip().split(',') for x in input.readlines()][0]
input = [int(x) for x in input]

input_test = [3, 4, 3, 1, 2]

INPUT = input


# DAY 6 PUZZLE 1

TOTAL_DAYS = 80

res_array = INPUT[:]
for day in range(1, TOTAL_DAYS + 1):
    temp = []
    for el in res_array:
        if(el > 0): temp.append(el - 1)
        if(el == 0):
            temp.append(6)
            temp.append(8)
    res_array = temp[:]

res1 = len(res_array)
print('DAY 6 PUZZLE 1: %d' % (res1))


# DAY 6 PUZZLE 2

TOTAL_DAYS = 256

res_array = np.array(INPUT[:])

res_dict = dict()
for i in range(0, 9):
    res_dict[i] = np.count_nonzero(res_array == i)

for day in range(1, TOTAL_DAYS + 1):
    count_zero = res_dict[0]
    for i in range(0, 8):
        res_dict[i] = res_dict[i+1]
    res_dict[6] += count_zero
    res_dict[8] = count_zero

res2 = sum(res_dict.values())
print('DAY 6 PUZZLE 2: %d' % (res2))