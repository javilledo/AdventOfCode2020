# READ DATA
INPUT = open('09.txt', 'r')
INPUT = [int(x.strip()) for x in INPUT.readlines()]

# FUNCTION CHECK NUMBER
def check_number(number, list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            a = list[i]
            b = list[j]
            if number == a + b:
                return True
    return False

# CODE FOR PUZZLE 1
preamble = 25
index_for_number_found_in_puzzle_1 = 0
number_found_in_puzzle_1 = 0
for index in range(preamble, len(INPUT)):
    number_checked = INPUT[index]
    if check_number(number_checked, INPUT[index-preamble:index]) == False:
        index_for_number_found_in_puzzle_1 = index
        number_found_in_puzzle_1 = number_checked

print('DAY 9 PUZZLE 1: %d' % (number_found_in_puzzle_1))

# CODE FOR PUZZLE 2
solution_array_puzzle_2 = []
for index in range (index_for_number_found_in_puzzle_1, 0, -1):
    sum = 0
    temp = []
    for i in range (index - 1, 0, -1):
        el = INPUT[i]
        sum += el
        temp.append(el)
        if sum == number_found_in_puzzle_1:
            solution_array_puzzle_2.append(temp)
            break
        elif sum > number_found_in_puzzle_1:
            break

solucion_puzzle_2 = max(solution_array_puzzle_2[0]) + min(solution_array_puzzle_2[0])
print('DAY 9 PUZZLE 2: %d' % (solucion_puzzle_2))