# READ DATA
INPUT = open('01.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [int(x) for x in INPUT]

# DAY 1 PUZZLE 1
solution = False
for i in INPUT:
    for j in INPUT:
        if (j != i) and (i + j == 2020) and (solution == False):
            print('DAY 1 PUZZLE 1: %d' % (i * j))
            solution = True

# DAY 1 PUZZLE 2
solution = False
for i in INPUT:
    for j in INPUT:
        for k in INPUT:
            if (j != i) and (j != k) and (i != k) and (i + j + k == 2020) and (solution == False):
                print('DAY 1 PUZZLE 2: %d' % (i * j * k))
                solution = True
