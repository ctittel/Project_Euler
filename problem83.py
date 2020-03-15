import numpy as np

with open('p083_matrix.txt') as f:
    cell_cost = f.read()

cell_cost = cell_cost.split('\n')
cell_cost = cell_cost[:-1]
cell_cost = [[int(j) for j in i.split(',')] for i in cell_cost]

cell_cost = np.array(cell_cost)

print(cell_cost)

# 1. path cost = trivial cost to goal
# 2. iterate through all: they can keep their value or decide to go over neighbor

path_cost = np.zeros(cell_cost.shape)

# numpy: row, column
# print(cell_cost[0,1])

path_cost[79,79] = cell_cost[79, 79]
for column in range(78, -1, -1):
    path_cost[79, column] = cell_cost[79,column] + path_cost[79, column + 1]

# print(path_cost)
for row in range(78, -1, -1):
    path_cost[row, :] = cell_cost[row, :] + path_cost[row + 1, :]

# print(path_cost)
# print(cell_cost)

def update_cell(row, column):
    global cell_cost
    global path_cost

    vals = []

    if row > 0:
        vals.append(cell_cost[row, column] + path_cost[row - 1, column])
    if column > 0:
        vals.append(cell_cost[row, column] + path_cost[row, column - 1])
    if row < 79:
        vals.append(cell_cost[row, column] + path_cost[row + 1, column])
    if column < 79:
        vals.append(cell_cost[row, column] + path_cost[row, column + 1])

    path_cost[row, column] = min(vals)

count = 0
while True:
    s = np.sum(path_cost)

    for i in range(78, -1, -1):
        for j in range(79, i-1, -1):
            if i == j:
                update_cell(i, j)
            else:
                update_cell(i, j)
                update_cell(j, i)

    s_new = np.sum(path_cost)
    if not count % 100:
        print(count, ": Update = ", s - s_new)
    if s == s_new:
        break

print(path_cost[0,0])