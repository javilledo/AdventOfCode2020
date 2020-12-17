# READ DATA
INPUT = open('06.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

# ORGANIZE DATA BY GROUPS
data_by_grops = []
temp = ''
people = 0
people_array = []
for el in INPUT:
    if el  == '':
        data_by_grops.append(temp)
        temp = ''
        people_array.append(people)
        people = 0
    else:
        temp += el
        people +=1

data_by_grops.append(temp)
people_array.append(people)

# TOTAL COUNT
total_sum = 0
total_sum_02 = 0
for i, el in enumerate(data_by_grops):
    chars = dict()
    for c in el:
        if c in chars.keys():
            chars[c] += 1
        else:
            chars[c] = 1
    for char in chars.keys():
        if chars[char] == people_array[i]:
            total_sum_02 += 1
    total_sum += len(chars.keys())

print('DAY 6 PUZZLE 1: %d' % (total_sum))
print('DAY 6 PUZZLE 2: %d' % (total_sum_02))

