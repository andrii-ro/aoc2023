import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)

res = 0
for l in lines:
    print(l)
    temp = 0
    amount = 0
    groups = (" ".join(l.split(':')[1].split())).split(' | ')
    winNumbers = set(groups[0].split(' '))
    numbers = groups[1].split(' ')
    for n in numbers:
        if n in winNumbers:
            amount += 1
    if amount == 1:
        temp = 1
    elif amount > 1:
        temp = (2**(amount-1))
    print(temp)
    res += int(temp)
    print(winNumbers)
print(res)

