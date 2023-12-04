import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)

res = 0
width = len(lines[0])
height = len(lines)
for i in range(height):
    
    print("Line #" + str(i))
    tempNumber = ""
    flag = False
    for j in range(width):
        if lines[i][j].isnumeric():
            tempNumber += lines[i][j]
            # search
            if i+1 < height and (not lines[i+1][j].isnumeric() and not lines[i+1][j] == '.'):
                flag = True
            elif i-1 >= 0 and (not lines[i-1][j].isnumeric() and not lines[i-1][j] == '.'):
                flag = True
            elif j+1 < width and (not lines[i][j+1].isnumeric() and not lines[i][j+1] == '.'):
                flag = True
            elif j-1 >= 0 and (not lines[i][j-1].isnumeric() and not lines[i][j-1] == '.'):
                flag = True
                
            elif j-1 >= 0 and i-1 >=0 and (not lines[i-1][j-1].isnumeric() and not lines[i-1][j-1] == '.'):
                flag = True                
            elif j-1 >= 0 and i+1 < height and (not lines[i+1][j-1].isnumeric() and not lines[i+1][j-1] == '.'):
                flag = True                
            elif j+1 < width and i+1 < height and (not lines[i+1][j+1].isnumeric() and not lines[i+1][j+1] == '.'):
                flag = True                
            elif j+1 < width and i-1 >=0 and (not lines[i-1][j+1].isnumeric() and not lines[i-1][j+1] == '.'):
                flag = True
        else:
            if (flag and len(tempNumber) > 0):
                print(tempNumber)
                res += int(tempNumber)
            flag = False
            tempNumber = ''
    
            
        # print(i, j)
    if (flag and len(tempNumber) > 0):
        print(tempNumber)
        res += int(tempNumber) 
    
print(res)
    
    