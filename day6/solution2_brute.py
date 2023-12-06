file_name = "input.txt"
with open(file_name) as f:
    race_time = int("".join(f.readline().strip().split(":")[1].strip().split()))
    record_distance = int("".join(f.readline().strip().split(":")[1].strip().split()))


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

print((upper_bound - lower_bound) + 1)