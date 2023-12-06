import sys

with open("input.txt") as f:
    seeds = set([int(i) for i in f.readline().split(": ")[1].split()])  
    data = f.read().strip()

maps = [x.strip() for x in data.split("\n\n")]
for i, x in enumerate(maps):
    maps[i] = maps[i].split(":")
    maps[i] = [x.strip() for x in maps[i]]

# destinations = []
# for seed in seeds:
#     current_source = seed

#     for map_name, map_infos in maps:
#         current_destination = None

#         for map_info in map_infos.split("\n"):
#             destination_start, source_start, range_len = [int(i) for i in map_info.split()]
#             if current_source in range(source_start, source_start + range_len):
#                 current_destination = destination_start + (current_source - source_start)
#                 break

#         if current_destination is None:
#             current_destination = current_source
#         current_source = current_destination
        
#     destinations.append(current_destination)

# print(min(destinations))

for location in range(265018614 - 10000, sys.maxsize):
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

    if current_destination in seeds:
        print(location)
        break