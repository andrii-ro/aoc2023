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

m = 99999999999
seedsCopy = seeds
seeds = []

print("SEEDS:")
for i in range(0, len(seedsCopy), 2):
    seeds.append([seedsCopy[i], seedsCopy[i]+seedsCopy[i+1]-1])
print("SEEDS len:" + str(len(seeds)))
print(seeds)

for seedRange in seeds:
    print("new seed\n")
    # temp = seed
    rangesToConsider = [seedRange]
    for category in categories:
        print("new category")
        # catTemp = -1
        tempRangesToConsider = []
        for rangeToConsider in rangesToConsider:
            wholeModified = False
            for line in category:
                ran = line[2]
                startDest = line[0]
                startSource = line[1]
                destRange = [startDest, startDest + ran-1]
                sourceRange = [startSource, startSource + ran-1]
                print("line: " + str(line))
                print("sourceRange: " + str(sourceRange))
                print("rangeToConsider: " + str(rangeToConsider))
                if sourceRange[0] <= rangeToConsider[0] and rangeToConsider[1] <= sourceRange[1]:
                    # # modify whole set
                    dif = rangeToConsider[0] - sourceRange[0]
                    # rangeToConsider[1] = startDest + (rangeToConsider[1] - rangeToConsider[0])
                    # rangeToConsider[0] = startDest + dif
                    t = [0]*2
                    t[0] = startDest + dif
                    t[1] = startDest + dif + (rangeToConsider[1] - rangeToConsider[0])

                    tempRangesToConsider.append(t)
                    wholeModified = True
                    print("#1")
                elif sourceRange[1] < rangeToConsider[0] or rangeToConsider[1] < sourceRange[0]:
                    # keep the same

                    print("#2")
                    # if not rangeToConsider in tempRangesToConsider:
                    #     tempRangesToConsider.append(rangeToConsider)

                elif sourceRange[0] <= rangeToConsider[0] < sourceRange[1] < rangeToConsider[1]:
                    # # 2 new ranges
                    dif = rangeToConsider[0] - sourceRange[0]
                    length = sourceRange[1] - rangeToConsider[0]
                    t1 = [0]*2
                    t1[0] = startDest + dif
                    t1[1] = startDest + dif + length
                    tempRangesToConsider.append(t1)

                    # t2 = [0]*2
                    rangeToConsider[0] = rangeToConsider[0] + length + 1
                    # rangeToConsider[1] = rangeToConsider[1]
                    # tempRangesToConsider.append(t2)
                    # rMod = True

                    print("#4")
                elif rangeToConsider[0] < sourceRange[0] < rangeToConsider[1] <= sourceRange[1]:
                    # 2 new ranges
                    dif = sourceRange[0] - rangeToConsider[0]
                    length = rangeToConsider[1] - sourceRange[0]
                    t1 = [0]*2
                    t1[0] = startDest
                    t1[1] = startDest + length
                    tempRangesToConsider.append(t1)

                    # t2 = [0] * 2
                    # t2[0] = rangeToConsider[0]
                    # t2[1] = rangeToConsider[1] - length - 1
                    # t2 = [0] * 2
                    # rangeToConsider[0] = rangeToConsider[0]
                    rangeToConsider[1] = rangeToConsider[1] - length - 1
                    # tempRangesToConsider.append(t2)
                    # rMod = True
                    print("rangeToConsider: " + str(rangeToConsider))
                    print("#5")
                elif sourceRange[0] > rangeToConsider[0] and sourceRange[1] < rangeToConsider[1]:
                    # 3 new ranges
                    dif = sourceRange[0] - rangeToConsider[0]
                    length = rangeToConsider[1] - sourceRange[0]
                    # t1 = [0]*2
                    t2 = [0]*2
                    t3 = [0]*2

                    dif3 = rangeToConsider[1] - sourceRange[1]
                    t3[0] = rangeToConsider[1] - dif3 + 1
                    t3[1] = rangeToConsider[1]

                    dif1 = sourceRange[0] - rangeToConsider[0]
                    # rangeToConsider[0] = rangeToConsider[0]
                    rangeToConsider[1] = rangeToConsider[0] + dif1 - 1

                    t2[0] = startDest
                    t2[1] = startDest + sourceRange[1] - sourceRange[0]

                    # tempRangesToConsider.append(t1)
                    tempRangesToConsider.append(t2)

                    rangesToConsider.append(t3)
                    # tempRangesToConsider.append(t3)

                    print("#6")
                    # rMod = True
            if not wholeModified:
                tempRangesToConsider.append(rangeToConsider)

        rangesToConsider = tempRangesToConsider
        tempRangesToConsider = []
        print(rangesToConsider)

    for i, j in rangesToConsider:
        m = min(i, m)
    print(rangesToConsider)
print(m)


# print(categories)
