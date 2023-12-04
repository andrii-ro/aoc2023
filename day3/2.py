import re

def getNumber(i, j):
    global lines
    global width
    global linesCopy
    l,r = j-1, j+1
    li = []
    li.append(lines[i][j])
    temp = list(lines[i])
    temp[j] = '.'
    lines[i] = ''.join(temp)
    while True:
        # print("l, r")
        # print(l, r)
        if l < 0 and r > width:
            break
        if (l < 0 or not lines[i][l].isnumeric()) and (r >= width or not lines[i][r].isnumeric()):
            break
        
        if l >= 0 and lines[i][l].isnumeric():
            li.insert(0, lines[i][l])
            temp = list(lines[i])
            temp[l] = '.'
            lines[i] = ''.join(temp)
            l -= 1
        if r < width and lines[i][r].isnumeric():
            li.append(lines[i][r])
            temp = list(lines[i])
            temp[r] = '.'
            lines[i] = ''.join(temp)
            r += 1
    print(li)
    return (int)("".join(li))

lines = []
linesCopy = lines
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)

linesCopy = lines

res = 0
width = len(lines[0])
height = len(lines)
print('start')
for i in range(height):
    
    print("Line #" + str(i))
    tempNumber = ""
    flag = False
    for j in range(width):
        if lines[i][j] == '*':
            print(i, j)
            numbers = []
            # search
            if i+1 < height and lines[i+1][j].isnumeric():
                numbers.append(getNumber(i+1, j))
            if i-1 >= 0 and lines[i-1][j].isnumeric():
                numbers.append(getNumber(i-1, j))
            if j+1 < width and lines[i][j+1].isnumeric():
                numbers.append(getNumber(i, j+1))
            if j-1 >= 0 and lines[i][j-1].isnumeric():
                numbers.append(getNumber(i, j-1))
                
            if j-1 >= 0 and i-1 >=0 and lines[i-1][j-1].isnumeric():
                numbers.append(getNumber(i-1, j-1))               
            if j-1 >= 0 and i+1 < height and lines[i+1][j-1].isnumeric():
                numbers.append(getNumber(i+1, j-1))                
            if j+1 < width and i+1 < height and lines[i+1][j+1].isnumeric():
                numbers.append(getNumber(i+1, j+1))                
            if j+1 < width and i-1 >=0 and lines[i-1][j+1].isnumeric():
                numbers.append(getNumber(i-1, j+1))

            if len(numbers) == 2:
                res += numbers[0] * numbers[1]
            else:
                lines = linesCopy
            print("numbers: " + str(numbers))
            print(lines)
    
print(res)
    
    