import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]
 
print(lines)

res = 0
for s in lines:
    numbers = re.findall(r'\d', s)
    result = list(map(int, numbers))
    t = (result[0] * 10) + result[len(result)-1]
    res += t
print(res)
    
    