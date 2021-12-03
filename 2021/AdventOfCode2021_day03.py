# READ DATA
INPUT = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/03.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x for x in INPUT]

TEST = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

# DAY 1 PUZZLE 1
gamma_rate_array = [[0, 0] for el in INPUT[0]]
for el in INPUT:
    for i in range(0, len(el)):
        if(el[i] == '0'): gamma_rate_array[i][0] += 1
        if(el[i] == '1'): gamma_rate_array[i][1] += 1

binary_gamma_rate = ''
binary_epsilon_rate = ''
for el in gamma_rate_array:
    if(el[0] > el[1]): 
        binary_gamma_rate += '0'
        binary_epsilon_rate += '1'
    if(el[0] < el[1]): 
        binary_gamma_rate += '1'
        binary_epsilon_rate += '0'
gamma_rate = int(binary_gamma_rate, 2)
epsilon_rate = int(binary_epsilon_rate, 2)

res1 = gamma_rate * epsilon_rate
print('DAY 3 PUZZLE 1: %d' % (res1))

# DAY 1 PUZZLE 2

# res2 = 0
# print('DAY 3 PUZZLE 2: %d' % (res2))