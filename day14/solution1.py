with open("input.txt") as f:
    rocks = list(map(list, f.read().splitlines()))

# print("\n".join(rocks))

for i in range(len(rocks)):
    for j in range(len(rocks[i])):
        if rocks[i][j] == "O":
            # print(f"Rock found at ({i}, {j}) => ", end="")
            row = i
            while (row - 1 >= 0) and (rocks[row - 1][j] == "."):
                row -= 1
            # print((row, j))
            rocks[i][j] = "."
            rocks[row][j] = "O"

multiplier = len(rocks)
ans = 0
for i in range(len(rocks)):
    for j in range(len(rocks[i])):
        if rocks[i][j] == "O":
            ans += multiplier
    multiplier -= 1

print(ans)