
# READ DATA
INPUT = open('03.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

TEST = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
TEST2 = [['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg'], ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']]

alphabet_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43,'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

# DAY 3 PUZZLE 1
priorities = 0
for s in INPUT:

    middle = int(len(s)/2)
    s1 = s[:middle]
    s2 = s[middle:]

    items = []
    for c in s1:
        if c in s2:
            items.append(c)

    unique_items = list(set(items))

    priorities += sum([alphabet_values[i] for i in unique_items])

res1 = priorities

print('DAY 2 PUZZLE 1: %d' % (res1))

# DAY 3 PUZZLE 2
TEST_IN_GROUPS_OF_3 = [TEST[i:i+3] for i in range(0, len(TEST), 3)]
INPUT_IN_GROUPS_OF_3 = [INPUT[i:i+3] for i in range(0, len(INPUT), 3)]

priorities = 0
for s3 in INPUT_IN_GROUPS_OF_3:
    items = []
    for c in s3[0]:
        if ((c in s3[1]) and (c in s3[2])):
            items.append(c)

    unique_items = list(set(items))

    priorities += sum([alphabet_values[i] for i in unique_items])

res2 = priorities

print('DAY 3 PUZZLE 2: %d' % (res2))