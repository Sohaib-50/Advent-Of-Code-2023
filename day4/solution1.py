with open("input.txt", "r") as f:
    cards = f.read().split("\n")

cards = [line.split(":")[1] for line in cards]
cards = [line.split("|") for line in cards]
total_points = 0
for winnings, haves in cards:
    winnings = {eval(i) for i in winnings.strip().split()}
    haves = [eval(i) for i in haves.strip().split()]
    
    card_points = 0
    for num in haves:
        if num in winnings:
            if card_points == 0:
                card_points = 1
            else:
                card_points *= 2

    total_points += card_points

print(total_points)