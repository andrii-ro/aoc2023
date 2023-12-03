import re

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)


res = 0
for s in lines:
    sections = re.split(': ', s)
    print(sections)
    game_id = sections[0].split(' ')[1]
    games = sections[1].split('; ')
    print(games)
    flag = True
    for g in games:
        cubes = g.split(', ')
        for c in cubes:
            m = {'red': 12, 'green': 13, 'blue': 14}
            cube_name = c.split(' ')[1]
            cube_amount = int(c.split(' ')[0])
            m[cube_name] -= cube_amount
            if (m[cube_name] < 0):
                flag = False
                break;
    if flag:
        res += int(game_id)
    
print(res)
    
    