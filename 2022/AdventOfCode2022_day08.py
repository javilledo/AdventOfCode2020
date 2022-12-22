import numpy as np

# READ DATA
INPUT = open('08.txt', 'r')
INPUT = [list(x.strip()) for x in INPUT.readlines()]
INPUT = map(lambda x: map(lambda y: int(y), x), INPUT)
INPUT = [list(el) for el in INPUT]

TEST = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]

trees = np.zeros((len(TEST), len(TEST[0])), dtype=int)
input = np.array(TEST)

# DAY 3 PUZZLE 1 (SOLUTION AS LIST OF LISTS)
matrix = TEST
lenv = len(matrix)
lenh = len(matrix[0])
count_visible = 2 * lenh + 2 * lenv - 4
for h in range(1, lenh - 1):
    for v in range(1, lenv - 1):

        height = matrix[v][h]

        max_left = max([matrix[v][el] for el in range(h)])
        max_right = max([matrix[v][el] for el in range(h + 1, lenh)])
        max_top = max([matrix[el][h] for el in range(v)])
        max_bottom = max([matrix[el][h] for el in range(v + 1, lenv)])

        if((max_left < height) or (max_right < height) or (max_top < height) or (max_bottom < height)): count_visible += 1

res1 = count_visible

# DAY 3 PUZZLE 1 (SOLUTION WITH NUMPY MATRIX)
matrix = np.array(INPUT)
count_visible = 2 * len(matrix[0]) + 2 * (len(matrix) - 2)
for i in range(1, matrix.shape[0]-1):
    for j in range(1, matrix.shape[1]-1):
        tree_column = matrix[:, j] - matrix[i, j]
        tree_row = matrix[i, :] - matrix[i, j]
        routes = [tree_row[:j], tree_row[j+1:], tree_column[:i], tree_column[i+1:]]
        if sum(list(map(lambda route: (route<0).all(), routes))) > 0:
            count_visible += 1
res1 = count_visible

print('DAY 8 PUZZLE 1: %d' % (res1))

# DAY 3 PUZZLE 2
scenic_scores = np.zeros((len(matrix), len(matrix[0])), dtype=int)

def compute_scenic_score(route):
    big_trees_array = list(route >= 0)
    if True in big_trees_array:
        return big_trees_array.index(True) + 1
    else:
        return len(big_trees_array)

for i in range(1, matrix.shape[0]-1):
    for j in range(1, matrix.shape[1]-1):
        tree_column = matrix[:, j] - matrix[i, j]
        tree_row = matrix[i, :] - matrix[i, j]
        routes = [tree_row[j-1::-1], tree_row[j+1:], tree_column[i-1::-1], tree_column[i+1:]]
        scenic_scores[i,j] = np.prod(list(map(compute_scenic_score, routes)))
    
res2 = np.max(scenic_scores)

print('DAY 8 PUZZLE 2: %d' % (res2))