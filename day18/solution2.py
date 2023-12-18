with open("input.txt") as f:
    instructions = [line.split(" (#")[1].split(")")[0] for line in f.read().split("\n")]
    # instructions = [line.split(" (")[0].split() for line in f.read().split("\n")]

movements = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}


for i, instruction in enumerate(instructions):
    direction, distance = int(instruction[-1]), instruction[:-1]

    if direction == 0:
        direction  = "R"
    elif direction == 1:
        direction = "D"
    elif direction == 2:
        direction = "L"
    elif direction == 3:
        direction = "U"

    distance = int(distance, base=16)

    instructions[i] = (direction, distance)


# with open("input.txt") as f:
#     instructions = [line.split(" (")[0].split() for line in f.read().split("\n")]
# instructions = [[direction, int(distance)] for (direction, distance) in instructions]


current = (0, 0)
vertices = [current]
for direction, distance in instructions:
    x, y = movements[direction]
    current = (current[0] + (x * distance), current[1] + (y * distance))
    vertices.append(current)

# find area using shoelace formula
area = 0
for i in range(len(vertices) - 1):
    area += vertices[i][0] * vertices[i + 1][1]
    area -= vertices[i][1] * vertices[i + 1][0]
area = 0.5 * abs(area)

# find interior points using pick's theorem
outer_points = sum([distance for direction, distance in instructions])
inner_points = area + 1 - (outer_points / 2)

# total points = outer points + inner points
print(int(outer_points + inner_points))



