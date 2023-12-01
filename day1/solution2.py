input_file_name = "test_case.txt"

with open(input_file_name, "r") as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

sum_ = 0
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for i, line in enumerate(lines):
    nums_found = {}
    for num in numbers:
        if ((idx := line.find(num)) != -1):
            nums_found[idx] = numbers[num]

    actual_numbers = [(idx, c) for idx, c in enumerate(line) if c.isnumeric()]
    for idx, n in actual_numbers:
        nums_found[idx] = n

    max_idx = max(nums_found)
    min_idx = min(nums_found)
    num_for_line = f"{nums_found[min_idx]}{nums_found[max_idx]}"

    sum_ += eval(num_for_line)

with open("output2.txt", "w") as f:
    f.write(str(sum_))

print(sum_)
