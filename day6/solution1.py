file_name = "test_case.txt"
with open(file_name) as f:
    times = list(map(int, f.readline().strip().split(":")[1].strip().split()))
    distances = list(map(int, f.readline().strip().split(":")[1].strip().split()))

# for each race time
# for each possible button push time
# find distance = race_time - btn time * btn_time
# binary search ify it somehow


for i, race_time in enumerate(times):
    record_distance = distances[i]
    
    # find lower bound
    left = 0
    right = race_time
    while left <= right:
        btn_time = (left + right) // 2  # middle
        current_distance = (race_time - btn_time) * btn_time  # distance = time * speed
        prev_distance = (race_time - (btn_time - 1)) * (btn_time - 1)

        if current_distance > record_distance:
            if (prev_distance < record_distance):
                break
            right = btn_time - 1

    lower_bound = btn_time