
# READ DATA
input = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/08.txt', 'r')
input = [x.strip() for x in input.readlines()]
input = [x.split(' | ') for x in input]
input = [[el[0].split(), el[1].split()] for el in input]

input_test = [[['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']],
              [['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'], ['fcgedb', 'cgb', 'dgebacf', 'gc']], 
              [['fgaebd', 'cg', 'bdaec', 'gdafb', 'agbcfd', 'gdcbef', 'bgcad', 'gfac', 'gcb', 'cdgabef'], ['cg', 'cg', 'fdcagb', 'cbg']],
              [['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega'], ['efabcd', 'cedba', 'gadfec', 'cb']],
              [['aecbfdg', 'fbg', 'gf', 'bafeg', 'dbefa', 'fcge', 'gcbea', 'fcaegb', 'dgceab', 'fcbdga'], ['gecf', 'egdcabf', 'bgf', 'bfgea']],
              [['fgeab', 'ca', 'afcebg', 'bdacfeg', 'cfaedg', 'gcfdb', 'baec', 'bfadeg', 'bafgc', 'acf'], ['gebdcfa', 'ecba', 'ca', 'fadegcb']],
              [['dbcfg', 'fgd', 'bdegcaf', 'fgec', 'aegbdf', 'ecdfab', 'fbedc', 'dacgb', 'gdcebf', 'gf'], ['cefg', 'dcbef', 'fcge', 'gbcadfe']],
              [['bdfegc', 'cbegaf', 'gecbf', 'dfcage', 'bdacg', 'ed', 'bedf', 'ced', 'adcbefg', 'gebcd'], ['ed', 'bcgafe', 'cdgba', 'cbgef']],
              [['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'], ['gbdfcae', 'bgc', 'cg', 'cgb']],
              [['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc'], ['fgae', 'cfgab', 'fg', 'bagce']]]

INPUT = input

dict = {
    0: 6,
    1: 2,
    2: 5, 
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

# DAY 8 PUZZLE 1
temp = [el[1] for el in INPUT] # second elements of array
temp = [val for sublist in temp for val in sublist] # flatten list
temp = [len(el) for el in temp] # len of each element
res = 0

for el in temp:
    if(el == dict[1] or el == dict[4] or el == dict[7] or el == dict[8]):
        res += 1
res1 = res
print('DAY 8 PUZZLE 1: %d' % (res1))


# DAY 8 PUZZLE 2
def number_from_code(code):
    if('A' in code and 'B' in code and 'C' in code and 'D' in code and 'E' in code and 'F' in code and 'G' in code): return '8'
    elif('A' in code and 'B' in code and 'C' in code and 'E' in code and 'F' in code and 'G'in code): return '0'
    elif('A' in code  and 'B' in code and 'D' in code and 'E' in code and 'F' in code and 'G' in code): return '6'
    elif('A' in code and 'B' in code and 'C' in code and 'D' in code and 'F' in code and 'G' in code): return '9'
    elif('A' in code and 'C' in code and 'D' in code and 'F' in code and 'G' in code): return '3'
    elif('A' in code and 'C' in code and 'D' in code and 'E' in code and 'G' in code): return '2'
    elif('A' in code and 'B' in code and 'D' in code and 'F' in code and 'G' in code): return '5'
    elif('B' in code and 'C' in code and 'D' in code and 'F'in code): return '4'
    elif('A' in code and 'C' in code and 'F' in code): return '7'
    elif('C' in code and 'F' in code): return '1'

res = 0
for el in INPUT:

    # Determine number of ocurrences
    num_ocurrences = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for w in el[0]:
        for c in w:
            num_ocurrences[c] += 1

    # Make a dict to decode
    dict_to_decode = { 'A': '', 'B': '', 'C': '',  'D': '', 'E': '', 'F': '', 'G': '' }

    # In digits, num of ocurrences which are uniques are B: 6, E: 4, F: 9
    dict_to_decode['B'] = [key for key in num_ocurrences.keys() if num_ocurrences[key] == 6][0]
    dict_to_decode['E'] = [key for key in num_ocurrences.keys() if num_ocurrences[key] == 4][0]
    dict_to_decode['F'] = [key for key in num_ocurrences.keys() if num_ocurrences[key] == 9][0]

    # Obtain the rest from unique quantity of digits 1: CF, 4: BCDF, 7: ACF, 8: ABCDEFG
    dict_to_decode['C'] = [w for w in el[0] if len(w) == 2][0].replace(dict_to_decode['F'],'') # 1 have 2 digits and one of them is F (known) --> Determine C
    dict_to_decode['A'] = [w for w in el[0] if len(w) == 3][0].replace(dict_to_decode['C'],'').replace(dict_to_decode['F'],'') # 7 have 3 digits and two of them is CF (known) --> Determine A
    dict_to_decode['D'] = [w for w in el[0] if len(w) == 4][0].replace(dict_to_decode['B'],'').replace(dict_to_decode['C'],'').replace(dict_to_decode['F'],'') # 4 have 4 digits and three of them is BCF (known) --> Determine D
    dict_to_decode['G'] = [w for w in el[0] if len(w) == 7][0].replace(dict_to_decode['A'],'').replace(dict_to_decode['B'],'').replace(dict_to_decode['C'],'').replace(dict_to_decode['D'],'').replace(dict_to_decode['E'],'').replace(dict_to_decode['F'],'') # 8 have 7 digits and six of them is ABCDEF (known) --> Determine G
    
    dict_to_decode = {y:x for (x, y) in dict_to_decode.items()} # Switch keys per values (to decode)

    res_line = ''
    for word in el[1]:
        decoded_word = ''
        for c in word:
            decoded_word += dict_to_decode[c]
        res_line += number_from_code(decoded_word)
    res += int(res_line)
        
res2 = res
print('DAY 8 PUZZLE 2: %d' % (res2))