# IMPORT LIBRARIES
import re

# READ DATA
INPUT = open('02.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

amount_password_ok_01 = 0
amount_password_ok_02 = 0

for element in INPUT:

    # DATA WRANGLING
    key_val = element.split(': ')
    limits_char = key_val[0].split(' ')
    limits = limits_char[0].split('-')
    low_limit = int(limits[0])
    high_limit = int(limits[1])
    char = limits_char[1]
    val = key_val[1]    
    amount = len(re.findall(char, val))

    # DAY 2 PUZZLE 1
    if (amount >= low_limit) and (amount <= high_limit): 
        amount_password_ok_01 += 1
    
    # DAY 2 PUZZLE 2
    if (val[low_limit - 1] == char):
        if(val[high_limit - 1] != char):
            amount_password_ok_02 += 1
    elif (val[high_limit - 1] == char):
            amount_password_ok_02 += 1

print('DAY 2 PUZZLE 1: %d' % (amount_password_ok_01))
print('DAY 2 PUZZLE 2: %d' % (amount_password_ok_02))