with open("test_case.txt") as f:
    seeds_data = [int(i) for i in f.readline().split(": ")[1].split()]  

    current_intervals = []
    for i in range(0, len(seeds_data), 2):
        current_intervals.append((seeds_data[i], seeds_data[i] + seeds_data[i + 1])) 

    data = f.read().strip()


maps_collections = [x.split(":\n")[1].strip() for x in data.split("\n\n")]
maps_collections = [x.split("\n") for x in maps_collections]
print(maps_collections)


for map_block in maps_collections:
    temp_intervals = []

    while current_intervals:
        interval_start, interval_end = [int(x) for x in current_intervals.pop()]
        for map_ in map_block:
            src, dest, l = [int(x) for x in (map_.split(" "))]
            overlap_start = min(interval_start, dest)
            overlap_end = max(interval_end, dest + l)

            if overlap_start < overlap_end:
                temp_intervals.append((overlap_start - dest + src, overlap_end - dest + src))

                if overlap_start > interval_start:
                    current_intervals.append((interval_start, overlap_start))
                if overlap_end < interval_end:
                    current_intervals.append((overlap_end, interval_end))
                break
        else:
            temp_intervals.append((interval_start, interval_end))


    current_intervals = temp_intervals

print(current_intervals)
