with open('p081_matrix.txt') as f:
    cell_cost = f.read()

cell_cost = cell_cost.split('\n')
cell_cost = cell_cost[:-1]
cell_cost = [[int(j) for j in i.split(',')] for i in cell_cost]

def update_path_cost(row, column):
    if row >= 79:
        cell_cost[row][column] += cell_cost[row][column+1]
        # direction[row][column] = 0
    elif column >= 79:
        cell_cost[row][column] += cell_cost[row+1][column]
    else:
        if cell_cost[row][column+1] < cell_cost[row+1][column]:
            cell_cost[row][column] += cell_cost[row][column+1]
        else:
            cell_cost[row][column] += cell_cost[row+1][column]

for i in range(78, -1, -1):
    for j in range(79, i - 1, -1):
        if i != j:
            update_path_cost(i, j)
            update_path_cost(j, i)
        else:
            update_path_cost(i, j)

print(cell_cost[0][0])
        