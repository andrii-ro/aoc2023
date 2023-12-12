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

rowsExp = []
alreadyAddedAmount = 0
for i in range(height):
    hasG = False
    for j in range(width):
        if lines[i][j] == '#':
            hasG = True
    if not hasG:
        # print("insert i = " + str(i))
        rowsExp.append(i)

print()
for i in linesCopy:
    print(i)

colExp = []
for j in range(width):
    hasG = False
    for i in range(height):
        if lines[i][j] == '#':
            hasG = True
            break
    if not hasG:
        print("insert at j=" + str(j))
        colExp.append(j)

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
print("rowsExp: " + str(rowsExp))
print("colExp: " + str(colExp))
for i in combinations:

    print(i)
    # print(i[1][1])
    distance = max(i[0][0]-i[1][0], i[1][0] - i[0][0]) + max(i[0][1] - i[1][1], i[1][1] - i[0][1])
    col1 = i[0][1]
    col2 = i[1][1]
    row1 = i[0][0]
    row2 = i[1][0]

    for col in colExp:
        if col1 < col < col2 or col2 < col < col1:
            distance += 1000000-1
    for row in rowsExp:
        if row1 < row < row2 or row2 < row < row1:
            distance += 1000000-1


    print(distance)
    res += distance
print(res)


