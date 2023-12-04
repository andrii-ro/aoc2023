import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)

cards = {}
for i in range(1, len(lines)+1):
    cards[i] = 1

res = 0
for l in lines:
    print(l)
    amount = 0
    gameId = int((" ".join(l.split(':')[0].split())).split()[1])
    # print(gameId)
    groups = (" ".join(l.split(':')[1].split())).split(' | ')
    winNumbers = set(groups[0].split(' '))
    numbers = groups[1].split(' ')
    for n in numbers:
        if n in winNumbers:
            amount += 1
    # for i in range()
    for i in range(1, amount+1):
        cards[gameId + i] = cards[gameId + i] + cards[gameId]
    res += amount * cards[gameId]
    # print(res)
    print("Amount: " + str(amount))
    print("Res: " + str(res))
    print(cards)
    print()
print(res)
print(res + len(lines))

