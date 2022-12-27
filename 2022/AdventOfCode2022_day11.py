
# READ DATA INPUT
INPUT = open('11.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

# READ DATA TEST
TEST = open('11_test.txt', 'r')
TEST = [x.strip() for x in TEST.readlines()]

# DAY 11 PUZZLE 1

# initial values
info = [*TEST]
dict = {}
monkey = 0

# initial dict with values
for el in info:
    if el.startswith('Monkey'):
        monkey = int(el[7])
        dict[monkey] = {'times_inspected': 0}
    elif el.startswith('Starting items: '):
        values = el.split(': ')[1]
        values = values.split(', ')
        values = [int(el) for el in values]
        dict[monkey]['values'] = values
    elif el.startswith('Test: divisible by '):
        temp = el.replace('Test: divisible by ', '')
        dict[monkey]['test_is_divisible_by'] = int(temp)
    elif el.startswith('If true: throw to monkey '):
        dict[monkey]['if_true'] = int(el[-1])
    elif el.startswith('If false: throw to monkey '):
        dict[monkey]['if_false'] = int(el[-1])

# operations
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
      }

for i in range(20):
    for el in info:
        if el.startswith('Monkey'):
            monkey = int(el[7])
        if el.startswith('Operation: new = old '):
            operation = el.replace('Operation: new = old ', '')
            operation = operation.split(' ')
            for value in dict[monkey]['values']:
                if(operation[1] == 'old'):
                    factor = value
                else:
                    factor = int(operation[1])
                result = op[operation[0]](value, factor)
                result = result // 3
                if result % dict[monkey]['test_is_divisible_by'] == 0:
                    throw_monkey = dict[monkey]['if_true']
                    dict[throw_monkey]['values'].append(result)                    
                else:
                    throw_monkey = dict[monkey]['if_false']
                    dict[throw_monkey]['values'].append(result)
                dict[monkey]['times_inspected'] += 1
            dict[monkey]['values'] = []

res1 = [dict[monkey]['times_inspected'] for monkey in list(dict.keys())]
res1.sort(reverse=True)
res1 = res1[0] * res1[1]
print('DAY 10 PUZZLE 1: %d' % (res1))


# DAY 10 PUZZLE 2

#TODO: revisar esta parte, el resultado NO es correcto

import numpy as np

# initial values
info = [*TEST]
dict2 = {}
monkey = 0

# initial dict2 with values
for el in info:
    if el.startswith('Monkey'):
        monkey = int(el[7])
        dict2[monkey] = {'times_inspected': 0}
    elif el.startswith('Starting items: '):
        values = el.split(': ')[1]
        values = values.split(', ')
        dict2[monkey]['values'] = np.array([int(el) for el in values])
    elif el.startswith('Test: divisible by '):
        temp = el.replace('Test: divisible by ', '')
        dict2[monkey]['test_is_divisible_by'] = int(temp)
    elif el.startswith('If true: throw to monkey '):
        dict2[monkey]['if_true'] = int(el[-1])
    elif el.startswith('If false: throw to monkey '):
        dict2[monkey]['if_false'] = int(el[-1])

for i in range(20):
    for el in info:
        if el.startswith('Monkey'):
            monkey = int(el[7])
            values_arr = dict2[monkey]['values']
        elif el.startswith('Operation: new = old ') and (values_arr.shape[0] > 0):
            operation = el.replace('Operation: new = old ', '')
            operation = operation.split(' ')
            if(operation[0] == '+'):
                if(operation[1] == 'old'):
                    result_arr = values_arr * 2
                else:
                    result_arr = values_arr + int(operation[1])
            elif(operation[0] == '*'):
                if(operation[1] == 'old'):
                    result_arr = values_arr ** 2
                else:
                    result_arr = values_arr * int(operation[1])
            num_test_is_divisible    = dict2[monkey]['test_is_divisible_by']
            monkey_to_throw_if_true  = dict2[monkey]['if_true']
            monkey_to_throw_if_false = dict2[monkey]['if_false']
            for result in result_arr:
                if result % num_test_is_divisible == 0:
                    dict2[monkey_to_throw_if_true]['values'] = np.append(dict2[monkey_to_throw_if_true]['values'], result)
                else:
                    dict2[monkey_to_throw_if_false]['values'] = np.append(dict2[monkey_to_throw_if_false]['values'], result)
            dict2[monkey]['times_inspected'] += values_arr.shape[0]
            dict2[monkey]['values'] = np.array([])


res2 = [dict2[monkey]['times_inspected'] for monkey in list(dict2.keys())]
res2.sort(reverse=True)
res2 = res2[0] * res2[1]
print('DAY 10 PUZZLE 2: %d' % (res2))