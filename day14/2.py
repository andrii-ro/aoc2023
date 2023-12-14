import itertools
from functools import lru_cache

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

for i in lines:
    print(i)

#Custom Decorator function
from functools import lru_cache


def hash_list(l: list) -> int:
    __hash = 0
    for i, e in enumerate(l):
        __hash = hash((__hash, i, hash_item(e)))
    return __hash


def hash_dict(d: dict) -> int:
    __hash = 0
    for k, v in d.items():
        __hash = hash((__hash, k, hash_item(v)))
    return __hash


def hash_item(e) -> int:
    if hasattr(e, '__hash__') and callable(e.__hash__):
        try:
            return hash(e)
        except TypeError:
            pass
    if isinstance(e, (list, set, tuple)):
        return hash_list(list(e))
    elif isinstance(e, (dict)):
        return hash_dict(e)
    else:
        raise TypeError(f'unhashable type: {e.__class__}')


def my_lru_cache(*opts, **kwopts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            __hash = hash_item([id(func)] + list(args) + list(kwargs.items()))

            @lru_cache(*opts, **kwopts)
            def cached_func(args_hash):
                return func(*args, **kwargs)

            return cached_func(__hash)

        return wrapper

    return decorator

@my_lru_cache()
def rotate(array: list, direction: int) -> list:
    global width, height
    if direction == 0:  # up
        for i in range(height):
            for j in range(width):
                if array[i][j] == 'O':
                    upi = i - 1
                    while upi >= 0:
                        if array[upi][j] != '.':
                            upi += 1
                            break
                        else:
                            upi -= 1
                    upi = max(upi, 0)
                    array[i][j], array[upi][j] = array[upi][j], array[i][j]

    elif direction == 1:  # right
        for i in range(height):
            for j in range(width-1, -1, -1):
                if array[i][j] == 'O':
                    righti = j + 1
                    while righti < width:
                        if array[i][righti] != '.':
                            righti -= 1
                            break
                        else:
                            righti += 1
                    righti = min(width - 1, righti)
                    array[i][j], array[i][righti] = array[i][righti], array[i][j]
    elif direction == 2:  # down
        for i in range(height-1, -1, -1):
            for j in range(width):
                if array[i][j] == 'O':
                    downi = i + 1
                    while downi < height:
                        if array[downi][j] != '.':
                            downi -= 1
                            break
                        else:
                            downi += 1
                    downi = min(downi, height - 1)
                    array[i][j], array[downi][j] = array[downi][j], array[i][j]
    elif direction == 3:  # left
        for i in range(height):
            for j in range(width):
                if array[i][j] == 'O':
                    lefti = j - 1
                    while lefti >= 0:
                        if array[i][lefti] != '.':
                            lefti += 1
                            break
                        else:
                            lefti -= 1
                    lefti = max(0, lefti)
                    array[i][j], array[i][lefti] = array[i][lefti], array[i][j]
    # for i in lines:
    #     print(i)
    # print()

width = len(lines[0])
height = len(lines)
for i in range(1000000000):
    print(i)
    # for g in range()
    # print("rotate 0")
    rotate(lines, 0)
    # print("rotate 3")
    rotate(lines, 3)
    # print("rotate 2")
    rotate(lines, 2)
    # print("rotate 1")
    rotate(lines, 1)
    # for i in lines:
    #     print(i)
    # print()


print()
for i in lines:
    print(i)

res = 0
for i in range(height):
    c = height - i
    res += lines[i].count('O') * c
print(res)