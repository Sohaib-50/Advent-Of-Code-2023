file_name = "input.txt"
with open(file_name) as f:
    times = list(map(int, f.readline().strip().split(":")[1].strip().split()))
    distances = list(map(int, f.readline().strip().split(":")[1].strip().split()))

# for each race time
# for each possible button push time
# find distance = race_time - btn time * btn_time
ans = 1
for i, race_time in enumerate(times):
    record_distance = distances[i]
    
    # find lower bound
    lower_bound = 0
    while lower_bound <= race_time:
        current_distance = (race_time - lower_bound) * lower_bound  # distance = time * speed
        if current_distance > record_distance:
            break
        lower_bound += 1

    # find upper_bound
    upper_bound = race_time
    while upper_bound >= 0:
        current_distance = (race_time - upper_bound) * upper_bound  # distance = time * speed
        if current_distance > record_distance:
            break
        upper_bound -= 1
    
    ans *= (upper_bound - lower_bound) + 1

print(ans)