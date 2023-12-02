# read data
games = open("input.txt", "r").read().split("\n")

# clean up data
games = {i + 1: game for i, game in enumerate(games)}

for id_ in games:
    games[id_] = games[id_].split(": ")[1].split("; ")
    for i in range(len(games[id_])):
        games[id_][i] = games[id_][i].replace(" blue", "b").replace(" green", "g").replace(" red", "r").split(", ")

# solve
result = 0
for i, game in games.items():
    R_MAX = G_MAX = B_MAX = float('-inf')

    for attempt in game:
        for x in attempt:
            count, color = int(x[:-1]), x[-1::]
            if color == "r":
                R_MAX = max(R_MAX, count)
            elif color == "g":
                G_MAX = max(G_MAX, count)
            else:
                B_MAX = max(B_MAX, count)

    result += R_MAX * G_MAX * B_MAX
            

    
with open("output2.txt", "w") as f:
    f.write(str(result))
print(result)