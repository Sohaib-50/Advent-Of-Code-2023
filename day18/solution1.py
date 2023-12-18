with open("input.txt") as f:
    instructions = [line.split(" (")[0].split() for line in f.read().split("\n")]


def is_valid_position(position):
    x, y = position
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))

def write_grid_to_file(grid, file_name):
    with open(file_name, "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")
        

movements = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}

current = (0, 0)
marked = {current}
for direction, distance in instructions:
    move = movements[direction]
    for _ in range(int(distance)):
        current = (current[0] + move[0], current[1] + move[1])
        marked.add(current)

row_end = (max(marked, key=lambda x: x[0])[0]) + 1
col_end = (max(marked, key=lambda x: x[1])[1]) + 1
row_start = (min(marked, key=lambda x: x[0])[0])
col_start = (min(marked, key=lambda x: x[1])[1])

grid = [["#" if (i, j) in marked else "." for j in range(col_start, col_end)] for i in range(row_start, row_end)]



## flood fill insides
    
# find first boundary point
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            break
    else:
        continue
    break

if grid[i][j + 1] == ".":
    start = (i, j + 1)
elif grid[i + 1][j] == ".":
    start = (i + 1, j)
else:
    start = (i + 1, j + 1)


queue_frontier = [start]
while queue_frontier:
    
    x, y = queue_frontier.pop()
    grid[x][y] = "X"
    adjusted_x, adjusted_y = (x - row_start, y - col_start)
    marked.add((adjusted_x, adjusted_y))
    
    for move in list(movements.values()):
        new_x, new_y = (x + move[0], y + move[1])
        
        if is_valid_position((new_x, new_y)) and grid[new_x][new_y] == "." and (new_x - row_start, new_y - col_start) not in marked:
            queue_frontier.append((new_x, new_y))
            grid[new_x][new_y] = "X"

write_grid_to_file(grid, "output1.txt")
print(len(marked))
