# READ DATA
INPUT = open('./2024/01.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x for x in INPUT]

# DAY 1 PUZZLE 1
array_of_ids_01 = []
array_of_ids_02 = []

for el in INPUT:
    temp = el.split()
    array_of_ids_01.append(int(temp[0]))
    array_of_ids_02.append(int(temp[1]))

array_of_ids_01.sort()
array_of_ids_02.sort()

res1 = 0
for el1, el2 in zip(array_of_ids_01, array_of_ids_02):
    res1 += abs(el2 - el1)
    
print('DAY 1 PUZZLE 1: %d' % (res1))

# DAY 1 PUZZLE 2
res2 = 0
for el in array_of_ids_01:
    temp = el * array_of_ids_02.count(el)
    res2 += temp

print('DAY 1 PUZZLE 2: %d' % (res2))
