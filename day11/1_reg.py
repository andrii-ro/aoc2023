import re
from collections import Counter
import copy
import itertools
import numpy as np

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

for i in lines:
    print(i)

LEFT = [0, -1]
RIGHT = [0, 1]
UP = [-1, 0]
DOWN = [1, 0]

width = len(lines[0])
height = len(lines)

linesCopy = copy.deepcopy(lines)
# check rows

alreadyAddedAmount = 0
for i in range(height):
    hasG = False
    for j in range(width):
        if lines[i][j] == '#':
            hasG = True
    if not hasG:
        # print("insert i = " + str(i))
        linesCopy.insert(i+alreadyAddedAmount, ['.'] * width)
        alreadyAddedAmount += 1

print()
for i in linesCopy:
    print(i)

alreadyAddedAmount = 0
for j in range(width):
    hasG = False
    for i in range(height):
        if lines[i][j] == '#':
            hasG = True
            break
    if not hasG:
        print("insert at j=" + str(j))
        for i1 in range(len(linesCopy)):
            linesCopy[i1].insert(j+alreadyAddedAmount, '.')
        alreadyAddedAmount += 1

print()
for i in linesCopy:
    print(i)

width = len(linesCopy[0])
height = len(linesCopy)

points = []
for i in range(height):
    for j in range(width):
        if linesCopy[i][j] == '#':
            points.append([i, j])
print(points)

combinations = list(itertools.combinations(points, 2))
print("Combos: " + str(len(combinations)))

res = 0
for i in combinations:
    print(i)
    # print(i[1][1])
    distance = max(i[0][0]-i[1][0], i[1][0] - i[0][0]) + max(i[0][1] - i[1][1], i[1][1] - i[0][1])
    print(distance)
    res += distance
print(res)


