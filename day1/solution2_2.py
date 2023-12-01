input_file_name = "input.txt"

with open(input_file_name, "r") as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

sum_ = 0
nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
nums_start_chars = {num[0] for num in nums}

for line in lines:
    # print(f"On line {line}")
    first = None
    last = None
    
    # print("Starting chars")
    for i, c in enumerate(line):
        # print(f"\nChar: {c}")
        to_add = None

        if c.isnumeric():
            to_add = c

        else:
            # print({x: nums[x] for x in nums if x[0] == c})
            for word, digit in nums.items():
                
                l = len(word)
                # print(f"checking {digit, word}")
                if i + l <= len(line):  # within limit
                    # print(f"worked {digit, word}")
                    if line[i : i + l] == word:  # if match
                        # print("word", word, end=" ")
                        # print(f"worked {digit, word}")
                        to_add = digit
                        break

        if to_add:
            if first is None:
                first = to_add
            else:
                last = to_add
    
    # if (first is not None) and (last is None):
    #     last = first
    # print(f"{first}{last}")
    if last is None:
        last = first
    sum_ += int(f"{first}{last}")




with open("output2.txt", "w") as f:
    f.write(str(sum_))

print(sum_)
