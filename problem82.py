import numpy as np

with open('p082_matrix.txt') as f:
    cell_cost = f.read()

cell_cost = cell_cost.split('\n')
cell_cost = cell_cost[:-1]
cell_cost = [[int(j) for j in i.split(',')] for i in cell_cost]

# print(cell_cost)
cell_cost = np.array(cell_cost)
# print(cell_cost)
# print(cell_cost)

# print column 79
# print(cell_cost[:,79])

path_cost = cell_cost.copy()

def update_path_costs():
    global path_cost
    new_path_cost = np.zeros(path_cost.shape)
    for column in range(79, -1, -1):
        new_path_cost[:,column] = [new_cell_cost(i, column) for i in range(0, 80)]
    path_cost = new_path_cost

def new_cell_cost(row, column):
    global path_cost
    costs = []

    if column >= 79:
        return cell_cost[row, column]

    if row > 0: # up
        costs.append(path_cost[row-1, column])
    if row < 79: # down
        costs.append(path_cost[row+1, column])
    if column < 79: # right
        costs.append(path_cost[row, column+1])

    return cell_cost[row, column] + min(costs)

i = 0
while True:
    s = np.sum(path_cost)
    update_path_costs()
    s_new = np.sum(path_cost)
    if not i% 100:
        print(i, " Change: ", s_new - s)
    i += 1
    if s == s_new:
        break

print(min(path_cost[:,0]))

# not optimized but works