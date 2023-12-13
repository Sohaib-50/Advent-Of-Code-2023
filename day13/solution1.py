with open("input.txt") as f:
    patterns = f.read().split("\n\n")

def check_symmetry(grid, i, j):
    while (i >= 0) and (j < len(grid)):
        if grid[i] != grid[j]:
            return False

        i -= 1
        j += 1
    return True
        
ans = 0
for pattern in patterns:
    rows = list(map(list, pattern.split("\n")))
    columns = list(zip(*rows))

    # find horizontal line
    rows_above_horizontal = None
    for i in range(1, len(rows)):
        if rows[i] == rows[i - 1]:
            if check_symmetry(rows, i - 1, i):
                rows_above_horizontal = (i - 1) + 1
                break
    if rows_above_horizontal is not None:
        ans += rows_above_horizontal * 100
            


    # find vertical line
    columns_left_of_vertical = None
    for j in range(1, len(columns)):
        if columns[j] == columns[j - 1]:
            if check_symmetry(columns, j - 1, j):
                columns_left_of_vertical = (j - 1) + 1
                break
    if columns_left_of_vertical is not None:
        ans += columns_left_of_vertical

print(f"Answer: {ans}")




  

