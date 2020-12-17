# IMPORT LIBRARIES
import math

# READ DATA
INPUT = open('05.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]

def get_row(code):
    array = list(range(2**len(code)))
    for w in code:
        if w == 'F':
            array = array[:math.floor(len(array)/2)]
        elif w == 'B':
            array = array[math.ceil(len(array)/2):]
    return array[0]

def get_column(code):
    array = list(range(2**len(code)))
    for w in code:
        if w == 'L':
            array = array[:math.floor(len(array)/2)]
        elif w == 'R':
            array = array[math.ceil(len(array)/2):]
    return array[0]   
    
rows = []
columns = []
seatIDs = []
high_seatID = 0
for seat in INPUT:
    row = get_row(seat[:7])
    column = get_column(seat[-3:])
    seatID = row * 8 + column
    if high_seatID < seatID: high_seatID = seatID

    seatIDs.append(seatID)

seatIDs.sort()

for index, seat in enumerate(seatIDs):
    if index <= len(seatIDs) - 2:
        if not (seatIDs[index+1] == seat + 1):
            my_seat = seat + 1  

print('DAY 5 PUZZLE 1: %d' % (high_seatID))
print('DAY 5 PUZZLE 2: %d' % (my_seat))
