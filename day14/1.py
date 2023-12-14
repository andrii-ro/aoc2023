import itertools

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

for i in lines:
    print(i)

def rotate(array: list, direction: int) -> list:
    global width, height
    if direction == 0:  # up
        for i in range(height):
            for j in range(width):
                if array[i][j] == 'O':
                    upi = i - 1
                    while upi >= 0:
                        if array[upi][j] != '.':
                            upi += 1
                            break
                        else:
                            upi -= 1
                    upi = max(upi, 0)
                    array[i][j], array[upi][j] = array[upi][j], array[i][j]

    elif direction == 1:  # right
        for i in range(height):
            for j in range(width-1, -1, -1):
                if array[i][j] == 'O':
                    righti = j + 1
                    while righti < width:
                        if array[i][righti] != '.':
                            righti -= 1
                            break
                        else:
                            righti += 1
                    righti = min(width - 1, righti)
                    array[i][j], array[i][righti] = array[i][righti], array[i][j]
    elif direction == 2:  # down
        for i in range(height-1, -1, -1):
            for j in range(width):
                if array[i][j] == 'O':
                    downi = i + 1
                    while downi < height:
                        if array[downi][j] != '.':
                            downi -= 1
                            break
                        else:
                            downi += 1
                    downi = min(downi, height - 1)
                    array[i][j], array[downi][j] = array[downi][j], array[i][j]
    elif direction == 3:  # left
        for i in range(height):
            for j in range(width):
                if array[i][j] == 'O':
                    lefti = j - 1
                    while lefti >= 0:
                        if array[i][lefti] != '.':
                            lefti += 1
                            break
                        else:
                            lefti -= 1
                    lefti = max(0, lefti)
                    array[i][j], array[i][lefti] = array[i][lefti], array[i][j]
    # for i in lines:
    #     print(i)
    # print()

width = len(lines[0])
height = len(lines)
rotate(lines, 0)


print()
for i in lines:
    print(i)

res = 0
for i in range(height):
    c = height - i
    res += lines[i].count('O') * c
print(res)