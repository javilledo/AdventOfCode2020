
# READ DATA
INPUT = open('04.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x.split(',') for x in INPUT]

TEST = [['2-4','6-8'],['2-3','4-5'],['5-7','7-9'],['2-8','3-7'],['6-6','4-6'],['2-6','4-8']]

# DAY 3 PUZZLE 1

count_full_contained = 0

for pair in INPUT:

    range1 = pair[0].split('-')
    list1 = list(range(int(range1[0]), int(range1[1])+1))

    range2 = pair[1].split('-')
    list2 = list(range(int(range2[0]), int(range2[1])+1))

    if (set(list2).issubset(set(list1))): count_full_contained += 1
    elif (set(list1).issubset(set(list2))): count_full_contained += 1

res1 = count_full_contained

print('DAY 4 PUZZLE 1: %d' % (res1))

# DAY 3 PUZZLE 2

count_overlapping = 0

for pair in INPUT:

    range1 = pair[0].split('-')
    list1 = list(range(int(range1[0]), int(range1[1])+1))

    range2 = pair[1].split('-')
    list2 = list(range(int(range2[0]), int(range2[1])+1))

    for el in list1:
        if el in list2:
            count_overlapping += 1
            break

res2 = count_overlapping

print('DAY 4 PUZZLE 2: %d' % (res2))