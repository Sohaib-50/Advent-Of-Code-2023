with open("input.txt") as f:
    data = f.read().split("\n\n")
    line1 = [int(x) for x in data[0].strip().split()[1:]]
    ranges = []
    for i in range(0, len(line1), 2):
        ranges.append((line1[i], line1[i] + line1[i + 1]))
    maps = [x.split(":\n")[1]  for x in data[1:]]
    maps = [x.split("\n")  for x in maps]


# for each map type
for map_block in maps:
    temp = []

    # pass each seed (range) through each map in current map type
    # check each range against each mapping and try to map
    while ranges:
        range_start, range_end = ranges.pop()

        # for each map in the current map type
        for map_ in map_block:
            dest, src, l = list(map(int, map_.split()))

            overlap_start = max(src, range_start)
            overlap_end = min(src + l, range_end)

            # if the seed range we are checking overlaps (partially or fully) with the map we're checking
            # then find the translated region (after mapping) of the overlap, and add it 
            if overlap_end > overlap_start:
                translated_overlap_start = dest + (overlap_start - src)
                translated_overlap_end = dest + (overlap_end - src)
                temp.append((translated_overlap_start, translated_overlap_end))

                # add rest of the non overlapping parts if any back to ranges for further processing
                if overlap_start > range_start:
                    ranges.append((range_start, overlap_start))

                if overlap_end < range_end:
                    ranges.append((overlap_end, range_end))
                
                # if match was found for current range we can stop checking other maps
                break

        else:  # if no match found for current range, directly add to temp since its a 1:1 mapping
            temp.append((range_start, range_end))
        
    ranges = temp
        
print(sorted(ranges)[0][0])

