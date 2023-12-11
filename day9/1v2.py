import re
from collections import Counter

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)

def calc(numbers):
    if len(set(numbers)) == 1:
        return numbers[0]

    difs = []
    for i in range(0, len(numbers) - 1):
        difs.append(numbers[i + 1] - numbers[i])
    return numbers[-1] + calc(difs)

res = 0
for line in lines:
    numbers = [int(i) for i in line.split()]

    res += calc(numbers)

print(res)
