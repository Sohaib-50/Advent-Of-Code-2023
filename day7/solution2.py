from collections import Counter

with open("input.txt") as f:
    data = f.read().split('\n')
    data = [x.split() for x in data]


high_cards = []  
one_pairs =  []
two_pairs = []
three_kinds = []
full_houses = []
four_kinds = []
five_kinds = []


def find_category(hand):
    if len(set(hand)) == 1:
        return 1
    
    elif len(set(hand)) == 2:
        if 4 in Counter(hand).values():
            return 2
        else:
            return 3

    elif len(set(hand)) == 3:
        if 3 in Counter(hand).values():
            return 4
        else:
            return 5
    
    elif len(set(hand)) == 4:
        return 6
    
    else:
        return 7


def replace_joker(hand):
    if len(set(hand)) == 1:
        return hand
    
    replacements = []

    for char in set(hand):
        if char == 'J':
            continue

        new_hand = hand.replace("J", char)
        score = find_category(new_hand)
        replacements.append((new_hand, score))

    # return one with lowest score
    return sorted(replacements, key=lambda x: x[1])[0][0]

        

for x in data:
    hand, bid = x

    if "J" in hand:
        new_hand = replace_joker(hand)
        category = find_category(new_hand)
    else:
        category = find_category(hand)
        
    if category == 1:
        five_kinds.append((hand, bid))
    elif category == 2:
        four_kinds.append((hand, bid))
    elif category == 3:
        full_houses.append((hand, bid))
    elif category == 4:
        three_kinds.append((hand, bid))
    elif category == 5:
        two_pairs.append((hand, bid))
    elif category == 6:
        one_pairs.append((hand, bid))
    else:
        high_cards.append((hand, bid))



def bubble_sort(cards_list):
    # print(f"Before: {cards_list}")
    cards = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J"
    card_strengths = {x: i for i, x in enumerate(cards.split(', ')[::-1])}

    is_sorted = False
    i = len(cards_list)
    while (not is_sorted) and (i > 0):
        is_sorted = True
        for j in range(1, i):
            current = cards_list[j][0]
            prev = cards_list[j - 1][0]
            
            for k in range(len(current)):
                if card_strengths[current[k]] < card_strengths[prev[k]]:
                    # print(f"Swapping {cards_list[j]} and {cards_list[j - 1]} because {current[k]} < {prev[k]}")
                    cards_list[j], cards_list[j - 1] = cards_list[j - 1], cards_list[j]
                    is_sorted = False
                    break
                elif card_strengths[current[k]] > card_strengths[prev[k]]:
                    break

        i -= 1
    # print(f"After: {cards_list}")

bubble_sort(five_kinds)
bubble_sort(four_kinds)
bubble_sort(full_houses)
# print(f"Before: {three_kinds}")
bubble_sort(three_kinds)
# print(f"After: {three_kinds}")
# print(f"Before: {two_pairs}")
bubble_sort(two_pairs)
# print(f"After: {two_pairs}")
bubble_sort(one_pairs)
bubble_sort(high_cards)

rankings = high_cards + one_pairs + two_pairs + three_kinds + full_houses + four_kinds + five_kinds

# print(high_cards, one_pairs, two_pairs, three_kinds, full_houses, four_kinds, five_kinds)
score = 0
for i, x in enumerate(rankings):
    score += (i + 1) * int(x[1])
print(score)