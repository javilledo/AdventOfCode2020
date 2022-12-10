
# READ DATA
INPUT = open('06.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()][0]

TEST1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
TEST2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
TEST3 = 'nppdvjthqldpwncqszvftbrmjlhg'
TEST4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
TEST5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

# DAY 3 PUZZLE 1
for i in range(3, len(INPUT)+1):
    unique = ''.join(list(set([*INPUT[i-4: i]])))
    if len(unique) == 4: 
        res1 = i
        break

print('DAY 4 PUZZLE 1: %d' % (res1))

# DAY 3 PUZZLE 2
for i in range(13, len(INPUT)+1):
    unique = ''.join(list(set([*INPUT[i-14: i]])))
    if len(unique) == 14: 
        res2 = i
        break

print('DAY 4 PUZZLE 2: %d' % (res2))