import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]
 
print(lines)

res = 0
for s in lines:
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', s)
    print(numbers)
    fixed = []
    for n in numbers:
        if (not n.isdigit()):
            if (n == "one"):
                fixed.append('1')
            elif(n == "two"):
                fixed.append('2')
            elif(n == "three"):
                fixed.append('3')
            elif(n == "four"):
                fixed.append('4')
            elif(n == "five"):
                fixed.append('5')
            elif(n == "six"):
                fixed.append('6')
            elif(n == "seven"):
                fixed.append('7')
            elif(n == "eight"):
                fixed.append('8')
            elif(n == "nine"):
                fixed.append('9')
        else:
            fixed.append(n)
    print(fixed)
    result = list(map(int, fixed))
    # print(numbers)
    t = (result[0] * 10) + result[len(result)-1]
    res += t
print(res)
    
    