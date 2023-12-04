with open("input.txt", "r") as f:
    cards = f.read().split("\n")

cards = [line.split(":")[1] for line in cards]
cards = [line.split("|") for line in cards]
card_instances = {i + 1: 1 for i in range(len(cards))}

for i, (winnings, haves) in enumerate(cards):
    card_num = i + 1
    winnings = {eval(j) for j in winnings.strip().split()}
    haves = [eval(j) for j in haves.strip().split()]
    
    matchings = 0
    for num in haves:
        if num in winnings:
            matchings += 1
    
    # for instances_count in range(card_instances[card_num]): 
    for j in range(card_num + 1, card_num + 1 + matchings):
        card_instances[j] += card_instances[card_num]


print(sum(card_instances.values()))