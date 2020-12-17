# READ DATA
INPUT = open('03.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

amount_of_trees_01 = 0
for i, el in enumerate(INPUT):
    position = (i * 3) % len(el)
    if (el[position] == '#'):
        amount_of_trees_01 += 1
    
def amount_of_trees(right, down):
    temp = 0
    for i, el in enumerate(INPUT):
        if i % down == 0:
            position = int(((i/down) * right) % len(el))
            if (el[position] == '#'):
                temp += 1
    return temp

result_02 = amount_of_trees(1, 1)* amount_of_trees(3,1) * amount_of_trees(5,1) * amount_of_trees(7,1) * amount_of_trees(1,2)

print('DAY 3 PUZZLE 1: %d' % (amount_of_trees_01))
print('DAY 3 PUZZLE 2: %d' % (result_02)) 