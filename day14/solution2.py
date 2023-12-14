with open("input.txt") as f:
    rocks = list(map(list, f.read().splitlines()))

CYCLES = 1000000000
states = {tuple(tuple(row) for row in rocks): 0}

for cycle in range(1, CYCLES + 1):
    for direction in range(4):
        for i in range(len(rocks)):
            for j in range(len(rocks[i])):
                if rocks[i][j] == "O":
                    row = i
                    while (row - 1 >= 0) and (rocks[row - 1][j] == "."):
                        row -= 1
                    rocks[i][j] = "."
                    rocks[row][j] = "O"

        rocks = list(map(list, zip(*rocks)))
        rocks = [list(reversed(row)) for row in rocks]
    
    key = tuple(tuple(row) for row in rocks)
    if key in states:
        cycle_start = states[key]
        cycle_end = cycle
        break

    states[key] = cycle

print(f"Cycle {cycle_end} found to be a repeat of cycle {cycle_start}")
period = cycle_end - cycle_start
for i in range(cycle_start, cycle_end):
    if ((CYCLES - i) % period) == 0:
        print(f"{CYCLES}th cycle will be same as {i}th cycle.")
        break

for state in states:
    if states[state] == i:
        break

multiplier = len(state)
ans = 0
for i in range(len(state)):
    for j in range(len(state[i])):
        if state[i][j] == "O":
            ans += multiplier
    multiplier -= 1

print(f"Answer: {ans}")
