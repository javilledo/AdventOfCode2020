# READ DATA
INPUT = open('07.txt', 'r')
INPUT = [x.strip().strip('.') for x in INPUT.readlines()]

# DICTIONARY OF DATA
dict_of_bags = dict()
for el in INPUT:
    el = el.replace(' bags', '').replace(' bag', '')
    _temp = el.split(' contain ')
    _key = _temp[0]
    if _temp[1] == 'no other': 
        _temp_dict = 0
    else:
        _temp[1] = _temp[1].split(', ')
        _temp_dict = dict()
        for _temp_el in _temp[1]:
            _temp_value = int(_temp_el[0])
            _temp_key = _temp_el[2:]
            _temp_dict[_temp_key] = _temp_value
    dict_of_bags[_key] = _temp_dict

# RECURSIVE FUNCTION TO CHECK
def check_bag(bag, bags, amount, list_keys):
    for k,v in bags.items():
        if k == bag: 
            amount += 0
        else:
            if v != 0:
                if v.get(bag) is not None and k not in list_keys:
                    amount += 1
                    list_keys.append(k)
                    amount = check_bag(k, dict_of_bags, amount, list_keys)
    return amount    

# EXECUTION
TARGET = 'shiny gold'
amount = 0
list_keys = [] 
amount = check_bag(TARGET, dict_of_bags, amount, list_keys)

print('DAY 7 PUZZLE 1: %d' % (amount))

# RECURSIVE FUNCTION TO SUM
def count_bags(bag, bags, count, mult):
    el = bags[bag]
    if el != 0:
        for k,v in el.items():
            count += v * mult
            count = count_bags(k, dict_of_bags, count, v * mult)
    return count

count = 0
count = count_bags(TARGET, dict_of_bags, count, 1)
print('DAY 7 PUZZLE 2: %d' % (count))