import math

# READ DATA
input = open('/Users/usuario/Documents/GitHub/advent-of-code/2021/10.txt', 'r')
input = [x.strip() for x in input.readlines()]
input_test = ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '{([(<{}[<>[]}>{[]{[(<()>', '(((({<>}<{<{<>}{[]{[]{}', '[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]', '{<[[]]>}<{[{[{[]{()[[[]', '[<(<(<(<{}))><([]([]()', '<{([([[(<>()){}]>(<<{{', '<{([{{}}[<[[[<>{}]]]>[]]']

INPUT = input

# DAY 10 PUZZLE 1

points_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

res1 = 0

for line in INPUT:
    i = 0
    dict_code = {}
    for c in line:
        if((c == '(') or (c == '[') or (c == '{') or (c == '<')): 
            dict_code[i] = c
            i += 1
        if(((c == ')') and (dict_code[i - 1] == '(')) or ((c == ']') and (dict_code[i - 1] == '[')) or ((c == '}') and (dict_code[i - 1] == '{')) or ((c == '>') and (dict_code[i - 1] == '<'))): 
            del dict_code[i - 1]
            i -= 1
        elif (((c == ')') and (dict_code[i - 1] != '(')) or ((c == ']') and (dict_code[i - 1] != '[')) or ((c == '}') and (dict_code[i - 1] != '{')) or ((c == '>') and (dict_code[i - 1] != '<'))): 
            res1 += points_dict[c]
            break

print('DAY 10 PUZZLE 1: %d' % (res1))


# DAY 10 PUZZLE 2

dict_complementary = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

array_of_incomplete = []
array_of_res = []
for line in INPUT:
    is_corrupt = False
    i = 0
    dict_code = {}
    for c in line:
        if((c == '(') or (c == '[') or (c == '{') or (c == '<')): 
            dict_code[i] = c
            i += 1
        if(((c == ')') and (dict_code[i - 1] == '(')) or ((c == ']') and (dict_code[i - 1] == '[')) or ((c == '}') and (dict_code[i - 1] == '{')) or ((c == '>') and (dict_code[i - 1] == '<'))): 
            del dict_code[i - 1]
            i -= 1
        elif (((c == ')') and (dict_code[i - 1] != '(')) or ((c == ']') and (dict_code[i - 1] != '[')) or ((c == '}') and (dict_code[i - 1] != '{')) or ((c == '>') and (dict_code[i - 1] != '<'))): 
            res1 += points_dict[c]
            is_corrupt = True
            break     
    if(is_corrupt ==  False):
        characters_incomplete = list(dict_code.values())
        characters_incomplete.reverse()
        characters_incomplete = [dict_complementary[c] for c in characters_incomplete]
        characters_incomplete = ''.join(characters_incomplete)
        temp_res = 0
        for c in characters_incomplete:
            temp_res = temp_res * 5
            temp_res += points_dict[c]
        array_of_res.append(temp_res)

array_of_res.sort()

res2 = array_of_res[math.floor(len(array_of_res)/2)]
print('DAY 10 PUZZLE 2: %d' % (res2))