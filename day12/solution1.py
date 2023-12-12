
def count_possible_configurations(springs, damaged):
    if springs == "":
        if damaged == ():
            return 1
        else:
            return 0
        
    if damaged == ():
        if "#" in springs:
            return 0
        else:
            return 1
        
    configs = 0

    # treat as dot 
    if springs[0] in ("?", "."):
        configs += count_possible_configurations(springs[1:], damaged)
    
    # treat as #
    if springs[0] in ("?", "#"):
        damaging = damaged[0]
        remaining = len(springs)
        if ((remaining == damaging) and ("." not in springs)) or ((remaining > damaging) and ("." not in springs[:damaging]) and (springs[damaging] in ".?")):
            configs += count_possible_configurations(springs[damaging + 1:], damaged[1:])


    return configs

with open("input.txt", "r") as f:
    data = f.read().splitlines()

ans = 0
for row in data:
    springs, damaged = row.split(" ")
    damaged = tuple((int(x) for x in damaged.split(",")))
    ans += count_possible_configurations(springs, damaged)

print(ans)