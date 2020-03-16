import math
import time
# count = 0
M = 100

# classic = []

# for a in range(1, M+1):
#     for b in range(1, a+1):
#         for c in range(1, b+1):
#             L = math.sqrt(a**2 +b**2+c**2+2*b*c)
#             if int(L) == L:
#                 # print(a,b,c, " = ", L)
#                 classic.append((a, b+c, int(L)))
#                 # count += 1


# print(classic)

# - create many triplets
# - add reverses
# - add multiples
# - remove where first element too big
# - remove duplicates
# - count possible combinations for all

def num_combinations(t):
    a = t[0]
    b = t[1]

    if b > 2*a:
        return 0

    n = math.floor(b / 2)
    if b - 1 > a:
        n -= (b - 1) - a
    return n
start = time.time()
M = 2000
triples = []
for m in range(1,M):
    for n in range(1,m):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        # if 2*a >= (b+c):
        triples.append((a,b,c))

triples = triples + [(b,a,c) for a,b,c in triples]

triples_cache = set()
for a,b,c in set(triples):
    if 2*a >= b:
        k = 1
        while a*k <= M:
            triples_cache.add((a*k, b*k, c*k))
            k += 1

print("triples cache generated in ", time.time() - start, " seconds")

def combs_up_to(M):
    global triples_cache
    count = 0
    for a,b,c in triples_cache:
        if a <= M:
            count += num_combinations((a,b,c))

    # print(count)
    return count

# for m in range(1000, 10000):
#     c = combs_up_to(m)
#     print(m, c)
#     if c > 10**6:
#         break

print("Starting loop")
for m in range(2000, 2, -1):
    c = combs_up_to(m)
    print(m, " = ", c)
    if c < 10**6:
        break