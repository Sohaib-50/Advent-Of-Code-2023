# read data
games = open("input.txt", "r").read().split("\n")

# clean up data
games = {i + 1: game for i, game in enumerate(games)}

for id_ in games:
    games[id_] = games[id_].split(": ")[1].split("; ")
    for i in range(len(games[id_])):
        games[id_][i] = games[id_][i].replace(" blue", "b").replace(" green", "g").replace(" red", "r").split(", ")

# solve
R_MAX = 12
G_MAX = 13
B_MAX = 14
result = 0
for i, game in games.items():
    game_valid = True

    for attempt in game:
        attempt_valid = True
        for x in attempt:
            count, color = int(x[:-1]), x[-1::]
            max_ = None
            if color == "r":
                max_ = R_MAX
            elif color == "g":
                max_ = G_MAX
            else:
                max_ = B_MAX
            
            if count > max_:
                attempt_valid = False
                break
    
        if not attempt_valid:
            game_valid = False
            break
    
    if game_valid:
        # print(i)
        result += i
    
with open("output1.txt", "w") as f:
    f.write(str(result))
print(result)