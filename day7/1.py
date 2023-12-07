import re
from collections import Counter

def count(string):
    return dict(Counter(string))

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)
hands = []
cards = [i.split()[0] for i in lines]
bids = [int(i.split()[1]) for i in lines]

for i in range(len(cards)):
    hands.append([cards[i], bids[i]])

print(hands)

powers = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: []
}

for hand in hands:
    card = hand[0]
    symbols = set(card)
    print(symbols)
    if len(symbols) == 5: # only high card
        powers[0].append(hand)
    if len(symbols) == 4: # 1 pair
        powers[1].append(hand)
    if len(symbols) == 3: # triple or 2 pairs
        isTriple = False
        print(count(card).items())
        for sym, amount in count(card).items():
            if amount == 3:
                isTriple = True
        if isTriple:
            powers[3].append(hand)
        else:
            powers[2].append(hand)
    if len(symbols) == 2: #4ofk or full house
        is4ofk = False
        for sym, amount in count(card).items():
            if amount == 4:
                is4ofk = True
        if is4ofk:
            powers[5].append(hand)
        else:
            powers[4].append(hand)
    if len(symbols) == 1: #5ofk
        powers[6].append(hand)


print(powers)

alphabet = "AKQJT98765432"
alphabet = alphabet[::-1]
res = 0
rank = 1
for p in range(0, 7):
    group = powers[p]
    group = sorted(group, key=lambda item: [alphabet.index(c) for c in item[0]])
    for i in group:
        print("RANK #" + str(rank) + " item: " + i[0] + " value: " + str(i[1]))
        res += rank * i[1]
        rank += 1
print(res)
