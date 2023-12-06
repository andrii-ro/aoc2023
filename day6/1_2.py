import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)
races = []
times = [int(i) for i in lines[0].split(':')[1].strip().split()]
distances = [int(i) for i in lines[1].split(':')[1].strip().split()]
for i in range(len(times)):
    races.append([times[i], distances[i]])
print(times)
print(distances)
print(races)
sum = 1
for race in races:
    hold = 1
    options = 0
    while hold < race[0]:
        timeLeft = race[0]-hold
        if timeLeft * hold > race[1]:
            options += 1
        hold += 1
    sum *= options
# ar = [line for line in lines]
print(sum)
