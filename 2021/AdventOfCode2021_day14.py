
# READ DATA
INPUT = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/14.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT_POLYMER_TEMPLATE = INPUT[0]
INPUT_PAIR_INSERTION = INPUT[2:]

INPUT_TEST_POLYMER_TEMPLATE = 'NNCB'
INPUT_TEST_PAIR_INSERTION = ['CH -> B', 'HH -> N','CB -> H','NH -> C','HB -> C','HC -> B','HN -> C','NN -> C','BH -> H','NC -> B','NB -> B','BN -> B','BB -> N','BC -> B','CC -> N','CN -> C']

input_polymer_template = INPUT_TEST_POLYMER_TEMPLATE
input_pair_insertion = INPUT_TEST_PAIR_INSERTION

# DAY 14 PUZZLE 1

# def insertion_process(template, pair_insertion):

#     polymer_dictionary = {}
#     for el in pair_insertion:
#         temp = el.split(' -> ')
#         polymer_dictionary[temp[0]] = temp[0][0] + temp[1] + temp[0][1]

#     res_template = ''

#     temp_pair_characters = []
#     for i in range(len(template) - 1):
#         temp_pair_characters.append(template[i] + template[i+1])

#     for cc in temp_pair_characters:
#         res_template = res_template[:-1]
#         res_template += polymer_dictionary[cc]
    
#     return res_template

# template = input_polymer_template
# pair_insertion = input_pair_insertion
# for step in range(1, 11):
#     template = insertion_process(template, pair_insertion)
#     print('step:', step, 'length:', len(template))

# count_dictionary = {}
# for c in template:
#     if (c not in count_dictionary.keys()): count_dictionary[c] = 1
#     else: count_dictionary[c] += 1

# max = max(count_dictionary.values())
# min = min(count_dictionary.values())

# res1 = max - min
# print('DAY 13 PUZZLE 1: %d' % (res1))

# DAY 14 PUZZLE 2

template = input_polymer_template
pair_insertion = input_pair_insertion

polymer_dictionary = {}
for el in pair_insertion:
    temp = el.split(' -> ')
    polymer_dictionary[temp[0]] = temp[1]

pair_characters = []
character_quantity = {}
for i in range(len(template) - 1):
    pair_characters.append(template[i] + template[i+1])
    if(template[i] not in character_quantity.keys()): character_quantity[template[i]] = 1
    else: character_quantity[template[i]] += 1
if(template[-1] not in character_quantity.keys()): character_quantity[template[-1]] = 1
else: character_quantity[template[-1]] += 1

for cc in pair_characters:
    print(cc)

#TODO: FUNCIÓN RECURSIVA INPUT: CC Y STEP, Y CON LÓGICA DEL MAX_STEP


    





res2 = 0
print('DAY 14 PUZZLE 2: %d' % (res2))