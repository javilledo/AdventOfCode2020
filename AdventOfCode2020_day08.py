# READ DATA
INPUT = open('08.txt', 'r')
INPUT = [x.strip().strip('.') for x in INPUT.readlines()]

# ORGANIZE DATA
INSTRUCTIONS = [el.split(' ')[0] for el in INPUT]
VALUE = [int(el.split(' ')[1]) for el in INPUT]
DONE = [0 for el in INPUT]

# DEFINITION OF PLAY
def play(value, pos, instrucciones):
    temp_instructions = instrucciones[pos]
    temp_value = VALUE[pos]
    if temp_instructions == 'acc':
        DONE[pos] = 1
        value += temp_value
        pos += 1
    elif temp_instructions == 'jmp':
        DONE[pos] = 1
        pos += temp_value
    elif temp_instructions == 'nop':
        DONE[pos] = 1
        pos += 1    
    return value, pos

# EXECUTE CODE FOR PUZZLE 1
value = 0
pos = 0
while DONE[pos] == 0:
    value, pos = play(value, pos, INSTRUCTIONS)

print('DAY 8 PUZZLE 1: %d' % (value))

# EXECUTE CODE FOR PUZZLE 2
for index, instruction in enumerate(INSTRUCTIONS):
    INSTRUCTIONS_mod = [ins for ins in INSTRUCTIONS]
    if instruction == 'jmp':
        INSTRUCTIONS_mod[index] = 'nop'
    elif instruction == 'nop':
        INSTRUCTIONS_mod[index] = 'jmp'
    value = 0
    pos = 0
    DONE = [0 for el in INPUT]    
    while DONE[pos] == 0:
        if pos < (len(INSTRUCTIONS) - 1): 
            value, pos = play(value, pos, INSTRUCTIONS_mod)
        elif pos == (len(INSTRUCTIONS) - 1):
            print('DAY 8 PUZZLE 2: %d' % (value))
            break