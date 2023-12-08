import re
from collections import Counter

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)


gide = list(lines[0])
print(gide)

map = [item.split(" = ") for item in lines[2:]]

print(map)
mapHash = {}
for item in map:
    item[1] = item[1].replace('(', '').replace(')', '').split(', ')
    mapHash[item[0]] = item[1]

print(mapHash)

d = {
    'L': 0,
    'R': 1
}

k = 0

gideIndex = 0
startEl = 'AAA'
item = mapHash[startEl][d[gide[gideIndex]]]
if item != 'ZZZ':
    gideIndex += 1
    k += 1

while item != 'ZZZ':
    print("Element: " + item)
    # print("k: " + str(k))
    print("direction: " + str(d[gide[gideIndex]]))

    item = mapHash[item][d[gide[gideIndex]]]

    gideIndex = (gideIndex + 1) % len(gide)
    k += 1

print(k)