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

# destinations = []
min_dest = float('inf')
total_seeds = sum([x[1] for x in seeds_ranges])
count = 0
for i, (start, length) in enumerate(seeds_ranges):
    # print(f"{(i / len(seeds_ranges))}% done")
    for seed in range(start, start + length):
        current_source = seed
        # print(f"{round((count / total_seeds) * 100, 2)}% done")
        # count += 1

        for map_name, map_infos in maps:
            # print(f"Checking Map {map_name}")
            current_destination = None
            for map_info in map_infos.split("\n"):
                # print(map_info)
                destination_start, source_start, range_len = [int(i) for i in map_info.split()]
                # if current_source in range(source_start, source_start + range_len):
                if source_start <= current_source <= source_start + range_len:
                    current_destination = destination_start + (current_source - source_start)
                    break
            if current_destination is None:
                current_destination = current_source
                # print(f"Taking 1:1 Match -> {current_destination}")
            current_source = current_destination
            # print(f"Moved to {current_destination}")

        # print("Final Destination:", current_destination, "\n")
        # break
        min_dest = min(min_dest, current_destination)

print(min_dest)
