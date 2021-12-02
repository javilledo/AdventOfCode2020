# READ DATA
INPUT = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/02.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x.split(' ') for x in INPUT]

POSITION = [0, 0]

TEST = [['forward',  '5'], ['down', '5'], ['forward', '8'], ['up', '3'], ['down', '8'], ['forward', '2']]

# DAY 1 PUZZLE 1
for mov in INPUT:
    if(mov[0] == 'forward'): POSITION[0] += int(mov[1])
    if(mov[0] == 'down'): POSITION[1] += int(mov[1])
    if(mov[0] == 'up'): POSITION[1] -= int(mov[1])

res1 = POSITION[0] * POSITION[1]
print('DAY 2 PUZZLE 1: %d' % (res1))


# DAY 1 PUZZLE 2
POSITION = [0, 0, 0]
for mov in INPUT:
    if(mov[0] == 'down'): POSITION[2] += int(mov[1])
    if(mov[0] == 'up'): POSITION[2] -= int(mov[1])
    if(mov[0] == 'forward'): 
        POSITION[0] += int(mov[1])
        POSITION[1] += int(mov[1]) * POSITION[2]
res2 = POSITION[0] * POSITION[1]
print('DAY 2 PUZZLE 1: %d' % (res2))