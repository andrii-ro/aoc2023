import re
from collections import Counter
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10**6)

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

print(lines)
#
#
# linesCopy = [['*' for i in range(n)] for j in range(m)]


d = {
    '|' : [
        ['.', '|', '.'],
        ['.', '|', '.'],
        ['.', '|', '.'],
    ],
    '-' : [
        ['.', '.', '.'],
        ['-', '-', '-'],
        ['.', '.', '.'],
    ],
    'L' : [
        ['.', '|', '.'],
        ['.', 'L', '-'],
        ['.', '.', '.'],
    ],
    'J' : [
        ['.', '|', '.'],
        ['-', 'J', '.'],
        ['.', '.', '.'],
    ],
    '7' : [
        ['.', '.', '.'],
        ['-', '7', '.'],
        ['.', '|', '.'],
    ],
    'F' : [
        ['.', '.', '.'],
        ['.', 'F', '-'],
        ['.', '|', '.'],
    ],
    '.' : [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ],
    'S' : [
        ['S', 'S', 'S'],
        ['S', 'S', 'S'],
        ['S', 'S', 'S'],
    ]
}

tempLines = []
for line in lines:
    t = []
    for i in line:
        t.append(d[i])
    tempLines.append(t)
# print(exLines)
for i in tempLines:
    print(i)

exLines = []
for line in tempLines:
    for i in range(3):
        temp = []
        for originItem in line:
            # temp.append(originItem[i])
            temp += originItem[i]
        exLines.append(temp)

print()
for i in exLines:
    print(i)

lines = exLines.copy()
s = [0, 0]
for line in lines:
    if 'S' in line:
        s[0], s[1] = lines.index(line)+2, line.index('S')+1
        break
print("Start Position: ")
print(s)

#########


m = len(lines)
n = len(lines[0])

linesCopy = [['.' for i in range(n)] for j in range(m)]

step = [1, 0]
curPos = [s[0], s[1]]

print(lines)

LEFT = [0, -1]
RIGHT = [0, 1]
UP = [-1, 0]
DOWN = [1, 0]

cur = lines[curPos[0] + step[0]][curPos[1] + step[1]]
curPos = [curPos[0] + step[0], curPos[1] + step[1]]
k = 0
while cur != 'S':
    prevStep = step.copy()
    linesCopy[curPos[0]][curPos[1]] = '*'
    # step = [0, 0]
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

linesCopy[s[0]][s[1]] = '*'
linesCopy[s[0]][s[1]-1] = '*'
linesCopy[s[0]][s[1]+1] = '*'

linesCopy[s[0]-1][s[1]] = '*'
linesCopy[s[0]-1][s[1]-1] = '*'
linesCopy[s[0]-1][s[1]+1] = '*'

linesCopy[s[0]-2][s[1]] = '*'
linesCopy[s[0]-2][s[1]-1] = '*'
linesCopy[s[0]-2][s[1]+1] = '*'

print("After find path")
for i in linesCopy:
    print(''.join(i))

def iterative_dfs(matrix, start):

    rows, cols = len(matrix), len(matrix[0])
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        # Process the current node
        print(f"Visiting node {current}")
        visited.add(current)

        # Get neighbors
        row, col = current
        neighbors = [
            (row - 1, col),  # Up
            (row + 1, col),  # Down
            (row, col - 1),  # Left
            (row, col + 1)   # Right
        ]

        # Add valid neighbors to the stack
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < rows and 0 <= n_col < cols and matrix[n_row][n_col] == '.' and neighbor not in visited:
                linesCopy[n_row][n_col] = '/'
                stack.append(neighbor)


# exLines = []
# for line in lines:
#     for i in line:
#         if i == ''

visited = [[False for i in range(n)] for j in range(m)]
start_node = (0, 0)
iterative_dfs(linesCopy, start_node)
# dfs(1, 1, visited)
# for i in range(m):
#     for j in range(n):
        # dfs(i, j, visited)

print("formatted array: ")
for i in linesCopy:
    print(''.join(i))

res = 0
for i in range(0, m, 3):
    for j in range(0, n, 3):
        isEl = True
        for i1 in range(i, i+3):
            for j1 in range(j, j+3):
                # print(i, j, i1, j1)
                # print(lines[i])
                if not linesCopy[i1][j1] == '.':
                    isEl = False
        if isEl:
            res += 1
            for i1 in range(i, i + 3):
                for j1 in range(j, j + 3):
                    lines[i1][j1] = '/'

print('Final array')
for i in linesCopy:
    print(''.join(i))

print(res)
