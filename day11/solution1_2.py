
with open("input.txt") as f:
    grid = f.read().splitlines()
grid = [list(row) for row in grid]


# expand
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

for i, row_idx in enumerate(rows_to_expand):
    grid.insert(row_idx + i, list("." * len(grid[0])))

for i, col_idx in enumerate(cols_to_expand):
    for row_idx in range(len(grid)):
        grid[row_idx].insert(col_idx + i, "." )


galaxy_positions = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "#"]

galaxy_pairs = []
for i in range(len(galaxy_positions)):
    for j in range(i + 1, len(galaxy_positions)):
        galaxy_pairs.append((galaxy_positions[i], galaxy_positions[j]))


shortest_distances = []
for j, (start, end) in enumerate(galaxy_pairs):
    # manhattan distance
    shortest_distances.append(abs(start[0] - end[0]) + abs(start[1] - end[1]))

    
print(sum(shortest_distances), "shortest_distance")