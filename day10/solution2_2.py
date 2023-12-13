with open("test_case2.txt") as f:
    grid = f.read().splitlines()


# allowed ways to arrive at each element
allowed_arrivals = {
    "-": {"left", "right"},
    "|": {"up", "down"},
    "7": {"right", "up"},
    "J": {"right", "down"},
    "L": {"left", "down"},
    "F": {"left", "up"},
    ".": set()
}

# allowed element for each movement type
allowed_movements = {
    "up": {"|", "J", "L", "S"},
    "down": {"|", "7", "F", "S"},
    "left": {"-", "7", "J", "S"},
    "right": {"-", "L", "F", "S"},
}

# find start
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
            break

x, y = start
visited = {start}
queue = [start]

while queue:
    x, y = queue.pop(0)
    element = grid[x][y]

    # try to go up
    if (x - 1) >= 0 and (x - 1, y) not in visited and element in allowed_movements["up"] and "up" in allowed_arrivals[grid[x - 1][y]]:
        queue.append((x - 1, y))
        visited.add((x - 1, y))

    # try to go down
    if (x + 1) < len(grid) and (x + 1, y) not in visited and element in allowed_movements["down"] and "down" in allowed_arrivals[grid[x + 1][y]]:
        queue.append((x + 1, y))
        visited.add((x + 1, y))

    # try to go left    
    if (y - 1) >= 0 and (x, y - 1) not in visited and element in allowed_movements["left"] and "left" in allowed_arrivals[grid[x][y - 1]]:
        queue.append((x, y - 1))
        visited.add((x, y - 1))

    # try to go right
    if (y + 1) < len(grid[x]) and (x, y + 1) not in visited and element in allowed_movements["right"] and "right" in allowed_arrivals[grid[x][y + 1]]:
        queue.append((x, y + 1))
        visited.add((x, y + 1))

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i, j) in visited:
#             grid[i] = grid[i][:j] + "#" + grid[i][j + 1:]
#         else:
#             grid[i] = grid[i][:j] + "." + grid[i][j + 1:]

print("\n".join("".join(row) for row in grid))
print()


# fill in S
x, y = start
right = (x, y + 1)
left = (x, y - 1)
down = (x + 1, y)
up = (x - 1, y)

S = None
if (left in visited) and (right in visited):
    S = "-"
elif (up in visited) and (down in visited):
    S = "|"
elif (left in visited) and (down in visited):
    S = "7"
elif (left in visited) and (up in visited):
    S = "J"
elif (right in visited) and (down in visited):
    S = "F"
elif (right in visited) and (up in visited):
    S = "L"

grid[x] = grid[x][:y] + S + grid[x][y + 1:]
print("\n".join("".join(row) for row in grid))
print()


# make an expanded grid
expanded_grid = [["." for _ in range(len(grid[0]) * 2)] for _ in range(len(grid) * 2)]

for i in range(len(grid)):
    for j in range(len(grid[0])):

        if (i, j) not in visited:
            continue

        element = grid[i][j]
        target_pos = (i * 2, j * 2)

        for increment in (0, 1):
            target_pos = (target_pos[0] + increment, target_pos[1] + increment)
            # fill in the element
            expanded_grid[target_pos[0]][target_pos[1]] = element

            # fill in the rest of the element
            if element == "-":
                expanded_grid[target_pos[0]][target_pos[1] + 1] = "-"
                # expanded_grid[target_pos[0] + 1][target_pos[1]] = "-"
                # expanded_grid[target_pos[0] + 1][target_pos[1] + 1] = "-"
            elif element == "|":
                expanded_grid[target_pos[0] + 1][target_pos[1]] = "|"
                # expanded_grid[target_pos[0]][target_pos[1] + 1] = "|"
                # expanded_grid[target_pos[0] + 1][target_pos[1] + 1] = "|"
            elif element == "7":
                expanded_grid[target_pos[0]][target_pos[1] - 1] = "-"
                expanded_grid[target_pos[0] + 1][target_pos[1]] = "|"
            elif element == "J":
                expanded_grid[target_pos[0]][target_pos[1] - 1] = "-"
                expanded_grid[target_pos[0] - 1][target_pos[1]] = "|"
            elif element == "L":
                expanded_grid[target_pos[0]][target_pos[1] + 1] = "-"
                expanded_grid[target_pos[0] - 1][target_pos[1]] = "|"
            elif element == "F":
                expanded_grid[target_pos[0]][target_pos[1] + 1] = "-"
            expanded_grid[target_pos[0] + 1][target_pos[1]] = "|"

# flood fill the expanded grid
flood_start = None
for i in range(len(expanded_grid)):
    for j in range(len(expanded_grid[0])):
        if expanded_grid[i][j] == ".":
            flood_start = (i, j)
            break
    else:
        continue
    break

for i in range(len(expanded_grid)):
    for j in range(len(expanded_grid[0])):
        if expanded_grid[i][j] != ".":
            expanded_grid[i][j] = "#"

flood_queue = [flood_start]
flood_visited = set()
while flood_queue:

    x, y = flood_queue.pop()

    if (x < 0) or (y < 0) or (x >= len(expanded_grid)) or (y >= len(expanded_grid[0])) or (expanded_grid[x][y] != "."):
        continue

    expanded_grid[x][y] = "~"

    for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        flood_queue.append((x + a, y + b))


print("\n".join("".join(row) for row in expanded_grid))

ans = sum((row.count(".") for row in expanded_grid))
print(ans)