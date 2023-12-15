with open("input.txt") as f:
    steps = f.read().strip().split(",")
print(steps)


def hash(sequence):
    ans = 0
    for char in sequence:
        ans += ord(char)
        ans *= 17
        ans %= 256
    
    return ans

print(sum(hash(step) for step in steps))