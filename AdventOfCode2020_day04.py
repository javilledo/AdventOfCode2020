# IMPORT LIBRARIES
import re

# READ DATA
INPUT = open('04.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

data = []
temp = ''
for el in INPUT:
    temp += el + ' '
    if el == '':
        temp = temp[:-2]
        data.append(temp)
        temp = ''

data.append(temp)

valid_01 = 0
for el in data:
    if len(re.findall('byr:', el)) != 0:
        if len(re.findall('iyr:', el)) != 0:
            if len(re.findall('eyr:', el)) != 0:
                if len(re.findall('hgt:', el)) != 0:
                    if len(re.findall('hcl:', el)) != 0:
                        if len(re.findall('ecl:', el)) != 0:
                            if len(re.findall('pid:', el)) != 0:
                                valid_01 += 1

def data2dictionary(data):
    dictionary = dict()
    keyval = data.split(' ')
    for el in keyval:
        if el != '':
            key_val = el.split(':')
            dictionary[key_val[0]] = key_val[1]
    return dictionary

def check_if_valid(dictionary):

    valid = True
    keys = list(dictionary.keys())

    if not 'byr' in keys:
        valid = False        
    else:
        val = int(dictionary['byr'])
        if val < 1920 or val > 2002: valid = False
    
    if not 'iyr' in keys:
        valid = False
    else:
        val = int(dictionary['iyr'])
        if val < 2010 or val > 2020: valid = False
    
    if not 'eyr' in keys:
        valid = False
    else:
        val = int(dictionary['eyr'])
        if val < 2020 or val > 2030: valid = False
    
    if not 'hgt' in keys:
        valid = False
    else:
        str = dictionary['hgt']
        unit = str[-2:]
        val = str[:-2]
        if unit == 'cm':
            if int(val) < 150 or int(val) > 193: valid = False
        elif unit == 'in':
            if int(val) < 59 or int(val) > 76: valid = False
        else:
            valid = False

    if not 'hcl' in keys:
        valid = False
    else:
        val = dictionary['hcl']
        if not len(re.findall('#[0-9a-f]{6}', val)) == 1: valid = False

    if not 'ecl' in keys:
        valid = False
    else:
        w = dictionary['ecl']
        if not (w == 'amb' or w == 'blu' or w == 'brn' or w == 'gry' or w == 'grn' or w == 'hzl' or w == 'oth'): valid = False

    if not 'pid' in keys:
        valid = False
    else:
        str = dictionary['pid']
        if len(str) != 9: valid = False

    return valid

valid_02 = 0
for el in data:
    if check_if_valid(data2dictionary(el)):
        valid_02 += 1

print('DAY 4 PUZZLE 1: %d' % (valid_01))
print('DAY 4 PUZZLE 2: %d' % (valid_02))