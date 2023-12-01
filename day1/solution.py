input_file_name = "input.txt"

with open(input_file_name, "r") as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

sum_ = 0
numbers = []
for line in lines:
    numbers = [c for c in line if c.isnumeric()]
    sum_ += eval(f"{numbers[0]}{numbers[-1]}")

with open("output.txt", "w") as f:
    f.write(str(sum_))
print(sum_)