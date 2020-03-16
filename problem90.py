square_nums = [(0, 1), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (6, 4), (8, 1)]

def gen_dices(sides = 6, min_num = 0, max_num = 9):
    if sides == 1:
        # yield []
        # return
        for i in range(min_num, max_num + 1):
            j = i
            if i == 9: j = 6
            yield [j]
        return
    else:
        for i in range(min_num, max_num + 1):
            for d in gen_dices(sides - 1, i + 1, max_num):
                j = i
                if i == 9: j = 6
                yield [j] + d

dices = [d for d in gen_dices()]
assert len(dices) == 210

def check_dices(d1, d2):
    global square_nums
    for a, b in square_nums:
        if not (a in d1 and b in d2):
            if not (b in d1 and a in d2):
                # print("FAIL", d1, d2, a, b)
                return False
    # print("SUCCESS", d1, d2, a, b)
    return True

count = 0
i = 0

cubes = set()

for i, d1 in enumerate(dices):
    for d2 in dices[i+1:]:
        i += 1
        # print(d1,d2)
        if check_dices(d1,d2):
            # a = frozenset((tuple(d1),tuple(d2)))
            # cubes.add(a)
            count += 1
            # cubes.add(tuple(d1))
            # cubes.add(tuple(d2))
print(i)
print(count)

