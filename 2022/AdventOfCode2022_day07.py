
# READ DATA
INPUT = open('07.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x.split(' ') for x in INPUT]

TEST = ['$ cd /','$ ls','dir a','14848514 b.txt','8504156 c.dat','dir d','$ cd a','$ ls','dir e','29116 f','2557 g','62596 h.lst','$ cd e','$ ls','584 i','$ cd ..','$ cd ..','$ cd d','$ ls','4060174 j','8033020 d.log','5626152 d.ext','7214296 k']
TEST = [el.split(' ') for el in TEST]

# DAY 3 PUZZLE 1
directories = {}
path = []
for s in INPUT:
    if s[1] == 'cd':
        if s[2] == '..':
            path.pop()
        else:
            path.append(s[2])
    elif s[1] == 'ls':
        continue
    elif s[0] == 'dir':
        continue
    else:
        size = int(s[0])
        temp_path = ''
        for el in path:
            if(temp_path == ''): 
                temp_path = el
            else:
                temp_path = temp_path + '/' + el
            try:
                directories[temp_path] += size  
            except:
                directories[temp_path] = size  

res1 = 0
for v in directories.values():
    if v <=100000:
        res1 += v

print('DAY 7 PUZZLE 1: %d' % (res1))

# DAY 3 PUZZLE 2
outer_most_size = directories['/']
unused_space_size = 70000000 - outer_most_size
required_size_libered = 30000000 - unused_space_size
chosen_directories_to_delete = []
for v in directories.values():
    if v > required_size_libered:
        chosen_directories_to_delete.append(v)
chosen_directories_to_delete.sort()
res2 = chosen_directories_to_delete[0]

print('DAY 7 PUZZLE 2: %d' % (res2))