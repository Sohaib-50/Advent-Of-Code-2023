with open("input.txt", "r") as f:
    engine = f.read().split("\n")



# find coordinates of symbols
symbol_positions = []
for i in range(len(engine)):
    for j in range(len(engine[0])):
        current = engine[i][j]

        # if valid part number indicating symbol
        if (not current.isnumeric()) and (current != "."):
            symbol_positions.append((i, j))


# find possible part number positions
part_num_positions = set()
for i, j in symbol_positions:

    # possible movements
    movements = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    movements.remove((0, 0))

    for a, b in movements:
        x, y = (i + a), (j + b)
        if (x >= 0) and (x < len(engine)) and (y >= 0) and (y < len(engine[0])):
            part_num_positions.add((x, y))


# for each part number coordinate, find number, add to sum
# go to coordinate, go back till start of number in line, then start reading till end of number
# ensure removing coordinates from possible part number coordinates to avoid duplicate counting.
visited = set()
answer = 0
for i, j in part_num_positions:
    if (i, j) in visited:
        continue
    visited.add((i, j))
    if engine[i][j].isnumeric():
        # go back in line
        x = i
        y = j
        while (y > 0) and engine[x][y - 1].isnumeric():
            y -= 1
            visited.add((x, y))
        
        current_number = [engine[x][y]]
        while (y < len(engine[0]) - 1) and (engine[x][y + 1].isnumeric()):
            y += 1
            visited.add((x, y))
            current_number.append(engine[x][y])
        
        answer += eval("".join(current_number))  

print(answer)