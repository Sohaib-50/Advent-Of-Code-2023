import sys
with open("input.txt") as f:
    seeds_data = [int(i) for i in f.readline().split(": ")[1].split()]  

    seeds_ranges = []
    for i in range(0, len(seeds_data), 2):
        seeds_ranges.append((seeds_data[i], seeds_data[i + 1])) 

    data = f.read().strip()

maps = [x.strip() for x in data.split("\n\n")]
# maps_temp = [x.split("\n\n")[0] for x in maps]
for i, x in enumerate(maps):
    maps[i] = maps[i].split(":")
    maps[i] = [x.strip() for x in maps[i]]

for location in range(0, sys.maxsize):
    print(location)
    current_source = location

    for map_name, map_infos in maps[::-1]:
        current_destination = None

        for map_info in map_infos.split("\n"):
            destination_start, source_start, range_len = [int(i) for i in map_info.split()]
            if current_source in range(destination_start, destination_start + range_len):
                current_destination = source_start + (current_source - destination_start)
                break

        if current_destination is None:
            current_destination = current_source
        current_source = current_destination

    # check if current_destination is a seed
    for start, length in seeds_ranges:
        if current_destination in range(start, start + length):
            print(location)
            break
    else:
        continue
    break
