with open("input.txt") as f:
    histories = [x.split() for x in f.read().splitlines()]

for i, history in enumerate(histories):
    histories[i] = [int(x) for x in history]
    

answer = 0
for current in histories:
    extrapolated_value = current[-1]
    temp = [current[i + 1] - current[i] for i in range(0, len(current) - 1)]
  
    while not (len(set(temp)) == 1 and temp[0] == 0):
        # print(f"Temp: {temp}; Cond1: {len(set(temp)) == 1}; Cond2: {temp[0] == 0}")
        # print(temp)
        
        current = temp[:]
        temp = [current[i + 1] - current[i] for i in range(0, len(current) - 1)]
        extrapolated_value += current[-1]

    answer += extrapolated_value

print(answer)