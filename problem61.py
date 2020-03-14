from itertools import permutations
triangles = []

triag = lambda n: int(n*(n+1)*0.5)
square = lambda n: int(n**2)
pentagonal = lambda n: int(n*(3*n-1)*0.5)
hexagonal = lambda n: int(n*(2*n-1))
heptagonal = lambda n: int(n*(5*n-3)*0.5)
octagonal = lambda n: int(n*(3*n-2))

funs = [triag, square, pentagonal, hexagonal, heptagonal, octagonal]
vals = []

for fun in funs:
    vals.append([])
    n = 1
    while True:
        x = fun(n)
        if x > 10000:
            break
        if x > 999:
            vals[-1].append(x)
        n += 1

vals = [[str(i) for i in v] for v in vals]
front_parts = [[i[:2] for i in v] for v in vals]
# back_parts = [[i[2:] for i in v]) for v in vals]

# print(vals)
# print([len(x) for x in vals])

for perm in permutations(range(6), r=6):
    # remove all numbers which don't have a number that starts with these digits in the nex set
    # nums = {i: vals[d] for i, d in enumerate(perm)}
    good_sets = [[i] for i in vals[perm[0]]]

    for i in range(1, 6):
        new_good_sets = []
        for good_set in good_sets:
            follow_ups = [j for j in vals[perm[i]] if (j[:2] == good_set[-1][2:])]
            for follow_up in follow_ups:
                new_good_sets.append(good_set + [follow_up])
        good_sets = new_good_sets

        if len(good_sets) == 0:
            break
    if len(good_sets):
        for good_set in good_sets:
            if good_set[0][:2] == good_set[-1][2:]:
                print("DONE: ", good_set, sum([int(i) for i in good_set]))