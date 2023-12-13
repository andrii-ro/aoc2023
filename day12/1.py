import itertools

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip().split()) for line in f]

for i in lines:
    # i[0] = list(i[0])
    i[1] = [int(n) for n in i[1].split(',')]
    print(i)

def check(line: str, groups):
    # print(line, groups)
    groupIndex = 0
    res = [[key, len(list(group))] for key, group in itertools.groupby(line)]
    for i in res:
        if i[0] == '#':
            if groupIndex > len(groups)-1:
                return False
            if not groups[groupIndex] == i[1]:
                return False
            else:
                groupIndex += 1
    if groupIndex != len(groups):
        return False
    # print(groupIndex, line, groups)
    return True

def combine(template, options):
    template = template.replace('?', '{}')
    for opts in itertools.product(*options):
        yield template.format(*opts)

# print(check('..#..##.#', [1,2,1]))

# print(list(combine(".??..??...?##.", ['.', '#'])))
# print(list(combine('AB?D?', ['.#'] * 2)))
print()
res = 0
print("len to calculate: " + str(len(lines)))
ind = 0
for i in lines:
    print("line # " + str(ind))
    ind += 1
    # print("check: " + str(i))
    quesAmount = i[0].count('?')
    # indices = [i for i, x in enumerate(i[0]) if x == "?"]
    # print(indices)
    # i[0] = i[0].replace('?', '.')
    # print(i[0])
    if quesAmount > 0:
        combos = list(combine(i[0], ['.#'] * quesAmount))
        for combo in combos:
            if check(combo, i[1]):
                res += 1
    else:
        if check(i[0], i[1]):
            res += 1

print(res)
    # l = 0

