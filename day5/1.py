import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)
categories = []

seeds = [int(i) for i in lines[0].split(':')[1].strip().split()]
print(seeds)

lines = lines[2:]
print(lines)

tempItems = []
for i in range(len(lines)):
    if len(lines[i]) == 0:
        categories.append(tempItems)
        tempItems = []
    elif not lines[i][0].isnumeric():
        continue
    else:
        tempItems.append([int(num) for num in lines[i].split()])
categories.append(tempItems)

m = 999999999

for seed in seeds:
    print("new seed\n")
    temp = seed
    for category in categories:
        print("new category")
        catTemp = -1
        for line in category:
            ran = line[2]
            startDest = line[0]
            startSource = line[1]
            if startSource <= temp < startSource + ran:
                # map to dest
                dif = temp - startSource
                catTemp = dif + startDest
            print(temp)
        if catTemp > -1:
            temp = catTemp
        print("category final temp: " + str(temp))
    m = min(temp, m)

print(m)



# print(categories)
