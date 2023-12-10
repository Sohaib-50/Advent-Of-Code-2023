with open("input.txt") as f:
    grid = f.read().splitlines()


# allowed ways to arrive at each element
allowed_arrivals = {
    "-": {"left", "right"},
    "|": {"up", "down"},
    "7": {"right", "up"},
    "J": {"right", "down"},
    "L": {"left", "down"},
    "F": {"left", "up"},
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

print(len(visited) // 2)


