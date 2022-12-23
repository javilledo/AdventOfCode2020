import numpy as np
import matplotlib.pyplot as plt

# READ DATA INPUT
INPUT = open('10.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x.split(' ') for x in INPUT]

# READ DATA TEST
TEST = open('10_test.txt', 'r')
TEST = [x.strip() for x in TEST.readlines()]
TEST = [x.split(' ') for x in TEST]

TEST2 = [['noop'], ['addx', '3'], ['addx', '-5']]

# DAY 10 PUZZLE 1
arr = INPUT

cycle = 0
value = 1
dict = {0: 1} #[cycle: value after}

for el in arr:
    if el[0] == 'noop':
        cycle += 1
        dict[cycle] = value
    else:
        cycle += 1
        dict[cycle] = value
        cycle += 1
        value += int(el[1])
        dict[cycle] = value

res1 = 20 * dict[20-1] + 60 * dict[60-1] + 100 * dict[100-1] + 140 * dict[140-1] + 180 * dict[180-1] + 220 * dict[220-1]
print('DAY 10 PUZZLE 1: %d' % (res1))

# DAY 10 PUZZLE 2
temp = np.zeros((40, 6))
for k, v in dict.items():
    y = k // 40
    pos = k % 40
    if ((pos == v - 1) or (pos == v) or (pos == v + 1)):
        temp[pos][y] = 1
    pass
plt.imshow(temp.T)
plt.show()
res2 = 0
print('DAY 10 PUZZLE 2: %d' % (res2))