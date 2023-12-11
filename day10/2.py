import re
from collections import Counter
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(15000)

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

print(lines)

m = len(lines)
n = len(lines[0])

linesCopy = [['*' for i in range(n)] for j in range(m)]

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
    # lines[curPos[0]][curPos[1]] = k
    # step = [0, 0]  # todo calculate
    if cur == '|':
        linesCopy[curPos[0]][curPos[1]] = "┃"
        if prevStep == DOWN:
            step = DOWN
        elif prevStep == UP:
            step = UP
    elif cur == '-':
        linesCopy[curPos[0]][curPos[1]] = "━"
        if prevStep == RIGHT:
            step = RIGHT
        elif prevStep == LEFT:
            step = LEFT
    elif cur == 'L':
        linesCopy[curPos[0]][curPos[1]] = "┗"
        if prevStep == DOWN:
            step = RIGHT
        elif prevStep == LEFT:
            step = UP
    elif cur == 'J':
        linesCopy[curPos[0]][curPos[1]] = "┛"
        if prevStep == RIGHT:
            step = UP
        elif prevStep == DOWN:
            step = LEFT
    elif cur == '7':
        linesCopy[curPos[0]][curPos[1]] = "┓"
        if prevStep == UP:
            step = LEFT
        elif prevStep == RIGHT:
            step = DOWN
    elif cur == 'F':
        linesCopy[curPos[0]][curPos[1]] = "┏"
        if prevStep == UP:
            step = RIGHT
        elif prevStep == LEFT:
            step = DOWN

    k += 1
    curPos = [curPos[0] + step[0], curPos[1] + step[1]]
    cur = lines[curPos[0]][curPos[1]]

lines[curPos[0]][curPos[1]] = 'S'

def dfs(i, j, visited):
    global m, n, linesCopy
    if i < 0 or j < 0 or i > m - 1 or j > n - 1 or linesCopy[i][j] in 'S┏┓┛┗━┃' or visited[i][j]:
        return
    linesCopy[i][j] = '/'
    visited[i][j] = True
    dfs(i - 1, j, visited)  # Move left
    dfs(i + 1, j, visited)  # Move Right
    dfs(i, j - 1, visited)  # Move top
    dfs(i, j + 1, visited)  # Move bottom


visited = [[False for i in range(n)] for j in range(m)]
dfs(1, 1, visited)
# for i in range(m):
#     for j in range(n):
        # dfs(i, j, visited)

# calculated by hand
for i in linesCopy:
    print(''.join(i))
print(k)

print(k/2)
