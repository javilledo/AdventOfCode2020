# READ DATA
INPUT = open('02.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x for x in INPUT]

TEST = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

# DAY 2 PUZZLE 1
res1 = 0
for game in INPUT:
    is_possible = True
    id_game = int(game.split(':')[0].split(' ')[1])
    game = game.split(': ')[1].split('; ')
    for set in game:
        set = set.split(', ')
        for el in set:
            el = el.split(' ')
            if (el[1] == 'red' and int(el[0]) > 12): is_possible = False
            if (el[1] == 'green' and int(el[0]) > 13): is_possible = False
            if (el[1] == 'blue' and int(el[0]) > 14): is_possible = False
    if is_possible == True: res1 += id_game
print('DAY 2 PUZZLE 1: %d' % (res1))

# DAY 2 PUZZLE 2
res2 = 0
for game in INPUT:
    game = game.split(': ')[1].split('; ')
    min_red_quantity = 0
    min_green_quantity = 0
    min_blue_quantity = 0
    for set in game:
        set = set.split(', ')
        for el in set:
            el = el.split(' ')
            if (el[1] == 'red'): min_red_quantity = max(min_red_quantity, int(el[0]))
            if (el[1] == 'green'): min_green_quantity = max(min_green_quantity, int(el[0]))
            if (el[1] == 'blue'): min_blue_quantity = max(min_blue_quantity, int(el[0]))
            pass
    res2 += (min_red_quantity * min_green_quantity * min_blue_quantity)
print('DAY 2 PUZZLE 2: %d' % (res2))