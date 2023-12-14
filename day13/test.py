
# Part 1

with open('input.txt', 'r') as f:
    lines = f.readlines()
    grid = [list(line.strip()) for line in lines]
    
    # Find all valid lines of reflection
    reflections = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0])):
            if grid[i][j] != '.' and grid[i][j - 1] == '.' and grid[i][j + 1] == '.':
                reflections.append([i, j])
            if grid[i][j] != '.' and grid[i - 1][j] == '.' and grid[i + 1][j] == '.':
                reflections.append([i, j])
                
    # Calculate the score
    score = 0
    for i, j in reflections:
        if grid[i][j - 1] == '.' and grid[i][j + 1] == '.':
            score += 100 * (i - 1) + j
        if grid[i - 1][j] == '.' and grid[i + 1][j] == '.':
            score += j - 1
            
    print(score)
# ```

# ```python
# Part 2

# with open('input.txt', 'r') as f:
#     lines = f.readlines()
#     grid = [list(line.strip()) for line in lines]

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == '.':
#             continue
#         elif grid[i][j - 1] == '.' or grid[i][j + 1] == '.':
#             grid[i][j] = '|'
#         elif grid[i - 1][j] == '.' or grid[i + 1][j] == '.':
#             grid[i][j] = '-'
            
# # Find the starting point
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == '|':
#             start_i = i
#             start_j = j
#             break
            
# # Follow the path
# path = []
# i = start_i
# j = start_j
# while True:
#     path.append((i, j))
#     if grid[i][j - 1] == '-' and (i, j - 1) not in path:
#         j -= 1
#     elif grid[i][j + 1] == '-' and (i, j + 1) not in path:
#         j += 1
#     elif grid[i - 1][j] == '|' and (i - 1, j) not in path:
#         i -= 1
#     elif grid[i + 1][j] == '|' and (i + 1, j) not in path:
#         i += 1
#     else:
#         break
        
# # Print the path
# for i, j in path:
#     print(grid[i][j], end='')
# ```