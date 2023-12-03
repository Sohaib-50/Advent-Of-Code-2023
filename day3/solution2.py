with open("input.txt", "r") as f:
    engine = f.read().split("\n")



# find coordinates of symbols
symbol_positions = []
for i in range(len(engine)):
    for j in range(len(engine[0])):
        current = engine[i][j]

        # if valid part number indicating symbol
        if current == "*":
            symbol_positions.append((i, j))


# find possible part number positions
part_num_positions = []
for i, j in symbol_positions:
    current_gear_positions = set()

    # possible movements
    movements = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    movements.remove((0, 0))

    for a, b in movements:
        x, y = (i + a), (j + b)
        if (x >= 0) and (x < len(engine)) and (y >= 0) and (y < len(engine[0])):
            current_gear_positions.add((x, y))

    part_num_positions.append(current_gear_positions)


# for each part number coordinate, find number, add to sum
# go to coordinate, go back till start of number in line, then start reading till end of number
# ensure removing coordinates from possible part number coordinates to avoid duplicate counting.
answer = 0
for positions in part_num_positions:
    visited = set()
    gear_nums = []
    for i, j in positions:
        if len(gear_nums) > 2:
            break
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
            
            gear_nums.append(eval("".join(current_number)))

    if len(gear_nums) == 2:
        answer += gear_nums[0] * gear_nums[1]
        print(gear_nums)
print(answer)