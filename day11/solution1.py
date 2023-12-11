
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
    queue = [start]
    visited = set()
    distance = 0
    print((start, end), round(j / len(galaxy_pairs) * 100, 2), "%")

    while queue:
        level_length = len(queue)
        for _ in range(level_length):
            x, y = queue.pop(0)
            visited.add((x, y))
            if (x, y) == end:
                break
            
            moves = []
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if ((i, j) not in visited) and (i >= 0) and (j >= 0) and (i < len(grid)) and (j < len(grid[0])):
                    moves.append((i, j))
            
            if moves:
                moves.sort(key=lambda move: ((move[0] - end[0]) ** 2 + (move[1] - end[1]) ** 2) ** 0.5)
                queue.append(moves[0])

        else:  # if no break
            distance += 1
            continue
        
        # if breaked from inner most for loop
        shortest_distances.append(distance)
        break 
    
print(sum(shortest_distances), "shortest_distance")