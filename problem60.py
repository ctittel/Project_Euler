from primes import primesfrom2to
import time
import itertools

start = time.time()

presumed_length = 4 # presumed max length of the primes

primes = primesfrom2to(10**(2*presumed_length))
primes = set([str(p) for p in primes if p > 10**presumed_length])

possible_primes = set([str(p) for p in primesfrom2to(10**presumed_length)])
print("Calculated primes in ", time.time()-start)

# 5 primes
# for every of these 5 primes:
# - there exist at least 5 other primes which end with them
# - there exist at least 5 other primes which start with them 

total_possible_pairs = []

# for p in possible_primes:    
#     possible_pairs = []

#     # p must have 8 possible pairs to be a possible prime
#     for pr in primes:
#         if len(pr) > len(p):
#             if pr.endswith(p) or pr.startswith(p):
#                 c = pr.replace(p, "")
#                 if c in primes:
#                     possible_pairs.append((p,c))
#     if len(possible_pairs) >= 8:
#         total_possible_pairs += possible_pairs
# print(total_possible_pairs)

def all_possible_splits(s, max_length):
    ''' Returns a list of tuples with all possible splits '''
    t = []
    l = len(s)
    for i in range(max(1, l - max_length), l - max(1, l - max_length)+1):
        t.append((s[:i], s[i:]))
    return t

# print(possible_primes)
# print(len(possible_primes))

# all_pairs = []
# for p in primes:
#     all_pairs += all_possible_splits(p, presumed_length)
#     # print(p, all_possible_splits(p, presumed_length))

# # remove all pairs which dont contain only primes
# prime_pairs = []
# for p1,p2 in all_pairs:
#     if not p1 in primes:
#         continue
#     if not p2 in primes:
#         continue
#     prime_pairs.append((p1,p2))

start = time.time()
prime_pairs = []
for p1 in possible_primes:
    for p in possible_primes:
        if p1 == p:
            continue
        if p1 + p in primes:
            prime_pairs.append((p1,p))
print("Found ", len(prime_pairs), " prime pairs in ", time.time() - start, " seconds")

# prime_pair_count_dict = {p:0 for p in possible_primes}
# for p1, p2 in prime_pairs:
#     prime_pair_count_dict[p1] += 1
#     prime_pair_count_dict[p2] += 1

# print(prime_pair_count_dict)
# primes_to_remove = []
# for k, v in prime_pair_count_dict.items():
#     print(k,v)
#     if v < 8:
#         primes_to_remove.append(k)
# primes_to_remove = set(primes_to_remove)
# print(primes_to_remove)

# print(len(prime_pairs))
start = time.time()
reduced_prime_pairs = []
for p in prime_pairs:
    if prime_pairs.count(p[::-1]):
        reduced_prime_pairs.append(p)
# print(len(reduced_prime_pairs))
# print(reduced_prime_pairs)
l = [p1 for p1, p2 in set(reduced_prime_pairs)]
candidates = set(l)
# print(l)
# print(len(set(l)))

# print(prime_pairs)
# print(t)

partners = {i:set() for i in candidates}
# print(partners)

for c in candidates:
    for p1, p2 in reduced_prime_pairs:
        if p1 == c:
            partners[c].add(p2)
print("Created partners set in ", time.time() - start, " seconds")
# print(partners)
possible_pair_sets = set()
for p1, p_rest in partners.items():
    a = [tuple([p1]) + tuple(i) for i in itertools.permutations(p_rest,4)]
    a = {frozenset(i) for i in a}
    # print(a)
    possible_pair_sets = possible_pair_sets.union(a)
# print(possible_pair_sets)

# Sort the frozensets according to their sum and find the smallest one which works
possible_pair_sets = list(possible_pair_sets)
# print(possible_pair_sets)

def sum_frozen_string_set(frozen_string_set):
    s = 0
    for i in frozen_string_set:
        s += int(i)
    return s

possible_pair_sets.sort(key=sum_frozen_string_set)
# print(possible_pair_sets)

for k,v in partners.items():
    v.add(k)
# print(partners)

for pair_set in possible_pair_sets:
    # check if the set is valid; if so we have the solution
    fail = False
    for s in pair_set:
        if not partners[s] >= pair_set:
            # print("FAIL", partners[s], pair_set)

            fail = True
        # else:
        #     print("SUCCESS", partners[s], pair_set)
    if not fail:
        print("SOLUTION: ", pair_set, " SUM: ", sum_frozen_string_set(pair_set))
        break