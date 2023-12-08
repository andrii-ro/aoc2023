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
# startEl = 'AAA'
curElements = []
ways = {}
for node in map:
    if node[0][-1:] == 'A':
        curElements.append(node[0])
        ways[node[0]] = []
print(curElements)

startElements = curElements.copy()
k = 0
# item = mapHash[startEl][d[gide[gideIndex]]]
# if item != 'ZZZ':
#     gideIndex += 1
#     k += 1
print(ways)
for g in range(10):
    # print()
    for i in range(len(startElements)):
        # print("direction: " + str(d[gide[gideIndex]]))
        # print("Element: " + curElements[i])
        ways[startElements[i]].append(curElements[i])
        curElements[i] = mapHash[curElements[i]][d[gide[gideIndex]]]
        # print()
    gideIndex = (gideIndex + 1) % len(gide)
# print(ways)
for key, value in ways.items():
    print()
    # print(key)
    last = 0
    for i in range(len(value)):
        if value[i][-1:] == 'Z':
            print(last - i)
            last = i
            print(f'index: {i}, value: {value[i]}')
    # print(i)


# i listed unique numbers above and found Least Common Multiple in online calculator :D