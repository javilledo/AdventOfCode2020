
# READ DATA
INPUT = open('01.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x for x in INPUT]

TEST = ['1000', '2000', '3000', '' , '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']

# DAY 1 PUZZLE 1
calories = []
calories_sum = 0
for el in INPUT:
    if el != '':
        calories_sum += int(el)
    else:
        calories.append(calories_sum)
        calories_sum = 0
calories.append(calories_sum)
res1 = max(calories)
print('DAY 1 PUZZLE 1: %d' % (res1))

# DAY 1 PUZZLE 2
calories.sort(reverse=True)
res2 = sum(calories[0:3])
print('DAY 1 PUZZLE 2: %d' % (res2))