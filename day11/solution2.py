
with open("input.txt") as f:
    grid = f.read().splitlines()
grid = [list(row) for row in grid]

rows_to_expand = []
cols_to_expand = []

for i, row in enumerate(grid):
    if set(row) == {"."}:
        rows_to_expand.append(i)
    
    col = []
    for j in range(len(grid[0])):
        col.append(grid[j][i])
    if set(col) == {"."}:
        cols_to_expand.append(i)


galaxy_positions = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "#"]

galaxy_pairs = []
for i in range(len(galaxy_positions)):
    for j in range(i + 1, len(galaxy_positions)):
        galaxy_pairs.append((galaxy_positions[i], galaxy_positions[j]))


shortest_distances = []
expansion_factor = 1000_000 - 1
for j, (start, end) in enumerate(galaxy_pairs):

    # manhattan distance

    count_rows_to_expand = 0
    for x in rows_to_expand:
        # if the row x lies between start and end
        if min(start[0], end[0]) < x < max(start[0], end[0]):
            count_rows_to_expand += 1

    count_cols_to_expand = 0
    for y in cols_to_expand:
        # if the col y lies between start and end
        if min(start[1], end[1]) < y < max(start[1], end[1]):
            count_cols_to_expand += 1
        

    rows_difference = abs(start[0] - end[0]) + count_rows_to_expand * expansion_factor
    cols_difference = abs(start[1] - end[1]) + count_cols_to_expand * expansion_factor

    shortest_distances.append(rows_difference + cols_difference)

    
print(sum(shortest_distances), "shortest_distance")