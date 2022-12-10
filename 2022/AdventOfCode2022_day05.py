
# READ DATA
INPUT_MOVEMENTS = open('05.txt', 'r')
INPUT_MOVEMENTS = [x.strip() for x in INPUT_MOVEMENTS.readlines()]

TEST_STACK = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
} 

INPUT_STACK = {
    1: ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B' ],
    2: ['D', 'W', 'B'],
    3: ['T', 'S', 'Q', 'W', 'J', 'C'],
    4: ['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
    5: ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
    6: ['B', 'W', 'F', 'T', 'N'],
    7: ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
    8: ['H', 'P', 'F', 'R'],
    9: ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']
}

TEST_MOVEMENTS = [ 'move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']

# DAY 3 PUZZLE 1

for m in INPUT_MOVEMENTS:

    temp = m[5:].split(' from ')
    movs = int(temp[0])
    temp = temp[1].split(' to ')
    init = int(temp[0])
    end = int(temp[1])

    for mov in range(movs):
        temp = INPUT_STACK[init][-1]
        INPUT_STACK[end].append(temp)
        INPUT_STACK[init].pop()

res1 = ''
for key in INPUT_STACK.keys():
    res1 += INPUT_STACK[key][-1]

print('DAY 4 PUZZLE 1: %s' % (res1))

# DAY 3 PUZZLE 2

INPUT_STACK = {
    1: ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B' ],
    2: ['D', 'W', 'B'],
    3: ['T', 'S', 'Q', 'W', 'J', 'C'],
    4: ['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
    5: ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
    6: ['B', 'W', 'F', 'T', 'N'],
    7: ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
    8: ['H', 'P', 'F', 'R'],
    9: ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']
}

for m in INPUT_MOVEMENTS:

    temp = m[5:].split(' from ')
    amount = int(temp[0])
    temp = temp[1].split(' to ')
    init = int(temp[0])
    end = int(temp[1])
    
    temp = INPUT_STACK[init][-amount:]
    INPUT_STACK[end] += temp
    for i in range(amount): INPUT_STACK[init].pop()
    
res2 = ''
for key in INPUT_STACK.keys():
    res2 += INPUT_STACK[key][-1]

print('DAY 5 PUZZLE 2: %s' % (res2))