with open("input.txt") as f:
    histories = [x.split() for x in f.read().splitlines()]

for i, history in enumerate(histories):
    histories[i] = [int(x) for x in history]
    

answer = 0
for current in histories:
    first_values = [current[0]]
    temp = [current[i + 1] - current[i] for i in range(0, len(current) - 1)]
    while not (len(set(temp)) == 1 and temp[0] == 0):
        current = temp[:]
        first_values.append(current[0])
        temp = [current[i + 1] - current[i] for i in range(0, len(current) - 1)]
    
    first_values.append(temp[0])
    first_values.reverse()

    extrapolated_value = 0
    for num in first_values[1:]:
        extrapolated_value = num - extrapolated_value
    
    answer += extrapolated_value

print(answer)