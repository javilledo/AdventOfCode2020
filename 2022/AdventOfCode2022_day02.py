
# READ DATA
INPUT = open('02.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x.split(' ') for x in INPUT]

TEST = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

# DAY 2 PUZZLE 1
score = 0
for el in INPUT:

    op = el[0]
    me = el[1]

    if(op == 'A'): #ROCK
        if(me == 'X'): #ROCK
            score += 1
            score += 3 #DRAW
        if(me == 'Y'): #PAPER
            score += 2
            score += 6 #WIN
        if(me == 'Z'): #SCISSORS
            score += 3
            score += 0 #LOSE
    if(op == 'B'): #PAPER
        if(me == 'X'): #ROCK
            score += 1
            score += 0 #LOSE
        if(me == 'Y'): #PAPER
            score += 2
            score += 3  #DRAW
        if(me == 'Z'): #SCISSORS
            score += 3
            score += 6 #WIN
    if(op == 'C'): #SCISSORS
        if(me == 'X'): #ROCK
            score += 1
            score += 6 #WIN
        if(me == 'Y'): #PAPER
            score += 2
            score += 0 #LOSE
        if(me == 'Z'): #SCISSORS
            score += 3
            score += 3 #DRAW

res1 = score

print('DAY 2 PUZZLE 1: %d' % (res1))

# DAY 2 PUZZLE 2
score = 0
for el in INPUT:

    op = el[0]
    me = el[1]

    if(op == 'A'): #ROCK
        if(me == 'X'): #LOSE
            score += 3 #SCISSORS
            score += 0
        if(me == 'Y'): #DRAW
            score += 1 #ROCK
            score += 3
        if(me == 'Z'): #WIN
            score += 2 #PAPER
            score += 6 
    if(op == 'B'): #PAPER
        if(me == 'X'): #LOSE
            score += 1 #ROCK
            score += 0 
        if(me == 'Y'): #DRAW
            score += 2 #PAPER
            score += 3 
        if(me == 'Z'): #WIN
            score += 3 #SCISSORS
            score += 6 
    if(op == 'C'): #SCISSORS
        if(me == 'X'): #LOSE
            score += 2 #PAPER
            score += 0 
        if(me == 'Y'): #DRAW
            score += 3 #SCISSORS
            score += 3
        if(me == 'Z'): #WIN
            score += 1 #ROCK
            score += 6 

res2 = score

print('DAY 2 PUZZLE 2: %d' % (res2))