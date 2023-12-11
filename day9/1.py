import re
from collections import Counter

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)

res = 0
for line in lines:
    numbers = []
    numbers.append([int(i) for i in line.split()])
    print()
    # print(numbers)

    difs = []
    for i in range(0, len(numbers[0]) - 1):
        difs.append(numbers[0][i + 1] - numbers[0][i])
    numbers.append(difs)
    print(numbers)
    # dif = []
    g = 1
    print(sum(numbers[g]))
    while sum(numbers[g]) != 0:
        difs = []
        for i in range(0, len(numbers[g])-1):
            difs.append(numbers[g][i+1] - numbers[g][i])

        numbers.append(difs)
        print(numbers)

        g += 1
    t = 0
    for i in range(len(numbers)-1, -1, -1):
        t += numbers[i][-1]

    print("t = " + str(t))
    res += t

print(res)
