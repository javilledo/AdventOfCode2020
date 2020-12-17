# IMPORT LIBRARIES
# from itertools import combinations

# READ DATA
INPUT = open('10.txt', 'r')
INPUT = [int(x.strip()) for x in INPUT.readlines()]

# CODE FOR PUZZLE 1
INPUT.sort()
result = []
for i in range(0, len(INPUT)-1):
    result.append(INPUT[i+1] - INPUT[i])

count_01 = len([el for el in result if el == 1]) + 1
count_03 = len([el for el in result if el == 3]) + 1
print('DAY 10 PUZZLE 1: %d' % (count_01 * count_03))

# OPTIMIZED VERSION FOR PUZZLE 2
sol = {0:1}
for element in sorted(INPUT):
    sol[element] = 0
    if element - 1 in sol:
        sol[element] += sol[element-1]
    if element - 2 in sol:
        sol[element] += sol[element-2]
    if element - 3 in sol:
        sol[element] += sol[element-3]
print ('DAY 10 PUZZLE 2: %d' % (sol[max(INPUT)]))

# CODE FOR PUZZLE 2
# test_01 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4] #result should be 8
# test_02 = [1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49] #result should be 19208

# def check_policy(list):
#     check_list = [list[i+1]-list[i] for i in range(len(list)-1)]
#     if check_list != []:
#         if max(check_list) < 4: 
#             return True

# def check_delete_one_element(list):
#     indexes = []
#     for i in range (1, len(list)-2):
#         temp_list = [el for el in list]
#         temp_list.pop(i)
#         if check_policy(temp_list): indexes.append(i)
#     return indexes

# def solve_puzzle_02(list):
#     list.sort()
#     list.insert(0,0)
#     list.append(list[len(list)-1]+3)
#     cases = 0
#     indexes = check_delete_one_element(list)
#     for i in range(1, len(indexes)+1):
#         for j in combinations(indexes, i):
#             temp_list = [el for el in list]
#             list_of_index = [el for el in j]
#             accum = 0
#             for index in list_of_index:
#                 temp_list.pop(index - accum)
#                 accum += 1
#             if check_policy(temp_list): cases += 1
#     return cases + 1 

# print ('DAY 10 PUZZLE 2: %d' % (solve_puzzle_02(INPUT)))