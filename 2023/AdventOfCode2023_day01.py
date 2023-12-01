    # READ DATA
INPUT = open('01.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x for x in INPUT]

TEST = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
TEST2 = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

# DAY 1 PUZZLE 1
res1 = 0
for el in INPUT:
    aux = [*el]
    temp = ''
    for i in aux:
        if i.isdigit(): temp += i
    temp = temp[0] + temp[-1]
    res1 += int(temp)
print('DAY 1 PUZZLE 1: %d' % (res1))

# DAY 1 PUZZLE 2
el_renamed = []
res2 = 0
for el in INPUT:
    el = el.replace('one', 'one1one')
    el = el.replace('two', 'two2two')
    el = el.replace('three', 'three3three')
    el = el.replace('four', 'four4four')
    el = el.replace('five', 'five5five')
    el = el.replace('six', 'six6six')
    el = el.replace('seven', 'seven7seven')
    el = el.replace('eight', 'eight8eight')
    el = el.replace('nine', 'nine9nine')
    temp = ''
    for i in el:
        if i.isdigit(): temp += i
    temp = temp[0] + temp[-1]
    res2 += int(temp)
print('DAY 1 PUZZLE 2: %d' % (res2))