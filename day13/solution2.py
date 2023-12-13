with open("input.txt") as f:
    patterns = f.read().split("\n\n")


def differs_by(grid, i, j):
    differences = 0
    for k in range(len(grid[i])):
        differences += grid[i][k] != grid[j][k]
    return differences


def is_reflective_with_1_smudge(pattern, i, j, smudges=0):
    if smudges > 1:
        return False
    
    if (i < 0) or (j >= len(pattern)):
        return smudges == 1
    
    differences = differs_by(pattern, i, j)

    if differences > 1:
        return False
    elif differences == 1:  # move ahead considering smudge
        return is_reflective_with_1_smudge(pattern, i - 1, j + 1,  smudges + 1)
    else:  # differs by 0 or in other words same
        return is_reflective_with_1_smudge(pattern, i - 1, j + 1, smudges)


ans = 0
for idx, pattern in enumerate(patterns):

    rows = list(map(list, pattern.split("\n")))
    rows_above_horizontal = None
    for i in range(1, len(rows)):
        if is_reflective_with_1_smudge(rows, i - 1, i):
            rows_above_horizontal = (i - 1) + 1
            break

    if rows_above_horizontal is not None:
        ans += rows_above_horizontal * 100
        continue
        

    columns = list(zip(*rows))
    columns_left_of_vertical = None
    for j in range(1, len(columns)):
        if is_reflective_with_1_smudge(columns, j - 1, j):
            columns_left_of_vertical = (j - 1) + 1
            break

    if columns_left_of_vertical is not None:
        # print(f"columns_left_of_vertical: {columns_left_of_vertical}")
        ans += columns_left_of_vertical

print(f"Answer: {ans}")







  

