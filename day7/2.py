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
    n = len(symbols)
    # if n > 1 and 'J' in symbols:
    #     n -= 1
    if n == 5: # only high card
        if 'J' in card:
            powers[1].append(hand) # pair
            continue
        powers[0].append(hand)
    if n == 4: # 1 pair
        if 'J' in card:
            powers[3].append(hand) # triple
            continue
        powers[1].append(hand)
    if n == 3: # triple or 2 pairs
        if 'J' in card:
            is4 = False
            for sym, amount in count(card).items():
                if amount == 1 and not sym == 'J':
                    is4 = True
            if is4:
                powers[5].append(hand)
            else:
                powers[4].append(hand)
            continue
        isTriple = False
        print(count(card).items())
        for sym, amount in count(card).items():
            if amount == 3:
                isTriple = True
        if isTriple:
            powers[3].append(hand)
        else:
            powers[2].append(hand)
    if n == 2: #4ofk or full house
        if 'J' in card:
            powers[6].append(hand) # triple
            continue
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

alphabet = "AKQT98765432J"
alphabet = alphabet[::-1]
res = 0
rank = 1
for p in range(0, 7):
    group = powers[p]
    group = sorted(group, key=lambda item: [alphabet.index(c) for c in item[0]])
    print()
    print(group)
    print()
    for i in group:
        print("p= " + str(p) + " RANK #" + str(rank) + " item: " + i[0] + " value: " + str(i[1]))
        res += rank * i[1]
        rank += 1
print(res)
