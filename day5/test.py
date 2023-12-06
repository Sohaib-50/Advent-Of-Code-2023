with open("input.txt") as f:
    seeds_data = [int(i) for i in f.readline().split(": ")[1].split()] 

seeds_ranges = []
for i in range(0, len(seeds_data), 2):
    seeds_ranges.append((seeds_data[i], seeds_data[i + 1]))
seeds_ranges.sort(key=lambda x: x[0])
print(seeds_ranges == sorted(seeds_ranges))