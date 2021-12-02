# READ DATA
INPUT = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/01.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [int(x) for x in INPUT]

TEST = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# DAY 1 PUZZLE 1
is_increased = [] 
for i in range(1, len(INPUT)):
    if(INPUT[i] - INPUT[i-1] > 0): 
        is_increased.append(True)
    else:
        is_increased.append(False)
res1 = sum(is_increased)
print('DAY 1 PUZZLE 1: %d' % (res1))

# DAY 1 PUZZLE 2
input_grouped = [INPUT[n:n+3] for n in range(0, len(INPUT))]
input_grouped_sum = [sum(el) for el in input_grouped]
is_increased = [] 
for i in range(1, len(input_grouped_sum)):
    if(input_grouped_sum[i] - input_grouped_sum[i-1] > 0): 
        is_increased.append(True)
    else:
        is_increased.append(False)
res2 = sum(is_increased)
print('DAY 1 PUZZLE 2: %d' % (res2))