import re
from collections import Counter

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

print(lines)

d = {
    '|': [[-1, 0], [1, 0]],
    '-': [[0, -1], [0, 1]],
    'L': [[-1, -1], [1, 1]],
    'J': [[-1, 1], [1, -1]],
    '7': [[-1, -1], [1, 1]],
    'F': [[-1, 1], [1, -1]],
}

s = [0, 0]
for line in lines:
    if 'S' in line:
        s[0], s[1] = lines.index(line), line.index('S')
print("Start Position: ")
print(s)



step = [1, 0]
curPos = [s[0], s[1]]


LEFT = [0, -1]
RIGHT = [0, 1]
UP = [-1, 0]
DOWN = [1, 0]

cur = lines[curPos[0] + step[0]][curPos[1] + step[1]]
curPos = [curPos[0] + step[0], curPos[1] + step[1]]
k = 0
while cur != 'S':
    prevStep = step.copy()
    lines[curPos[0]][curPos[1]] = '*'
    # step = [0, 0]  # todo calculate
    if cur == '|':
        if prevStep == DOWN:
            step = DOWN
        elif prevStep == UP:
            step = UP
    elif cur == '-':
        if prevStep == RIGHT:
            step = RIGHT
        elif prevStep == LEFT:
            step = LEFT
    elif cur == 'L':
        if prevStep == DOWN:
            step = RIGHT
        elif prevStep == LEFT:
            step = UP
    elif cur == 'J':
        if prevStep == RIGHT:
            step = UP
        elif prevStep == DOWN:
            step = LEFT
    elif cur == '7':
        if prevStep == UP:
            step = LEFT
        elif prevStep == RIGHT:
            step = DOWN
    elif cur == 'F':
        if prevStep == UP:
            step = RIGHT
        elif prevStep == LEFT:
            step = DOWN

    k += 1
    curPos = [curPos[0] + step[0], curPos[1] + step[1]]
    cur = lines[curPos[0]][curPos[1]]

for i in lines:
    print(i)
print(k)

print(k/2)
