from sympy import Idx


with open("input.txt") as f:
    steps = f.read().strip().split(",")

boxes = [dict() for _ in range(256)]

def hash(sequence):
    sequence = sequence.split("=")[0]
    sequence = sequence.split("-")[0]
    ans = 0
    for char in sequence:
        ans += ord(char)
        ans *= 17
        ans %= 256
    # print(ans)
    return ans


for step in steps:
    operation = "-" if "-" in step else "="
    label_str, label_num = step.split(operation)
    box_idx = hash(label_str)

  
    if operation == "-" and label_str in boxes[box_idx]:
        del boxes[box_idx][label_str]
    
    elif operation == "=":
        boxes[box_idx][label_str] = label_num
    

ans = 0
for i, box in enumerate(boxes):
    box_num = i + 1

    for j, lens in enumerate(box):
        ans += (box_num) * (j + 1) * int(box[lens])

print(ans)

    






