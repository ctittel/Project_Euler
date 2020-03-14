from primes import primesfrom2to

primes = primesfrom2to(10**7)
primes_set = set(primes)

def get_prime_divisors(x):
    divs = []
    
    if x in primes_set:
        yield x
        return

    for p in primes:
        if 2*p > x:
            if x in primes:
                yield x
            return
        if not x % p:
            yield p

# def p(x):
#     product = x
#     # print("Primes of ", x, " : ", get_prime_divisors(x))
#     for div in get_prime_divisors(x):
#         product *= (1 - (1/div))
#     return int(product)

def is_permutation(a,b):
    a = sorted(list(str(a)))
    b = sorted(list(str(b)))
    return a == b

def prime_prod(n, current_min):
    prod = 1
    for p in get_prime_divisors(n):
        prod /= (1 - (1/p))
        if prod > current_min:
            return False
    return prod, int(n/prod)

def get_largest_permutation(n):
    return int(''.join(sorted(str(n))[::-1]))

def calc_pn(n, prime_factors):
    f = n
    for p in prime_factors:
        f *= (1- (1/p))
    return int(f)

def calc_quotient(prime_factors):
    p = 1
    for f in prime_factors:
        p /= (1- (1/f))
    return p

    

best_min = 1000000
best_n = None
# for n in range(2,10**7):
# for n in primes[::-1]:

#     if (n/get_largest_permutation(n)) > best_min:
#         continue

#     r = prime_prod(n, best_min)
#     if r:
#         current_min, current_pn = r
#         if is_permutation(n, current_pn):
#             print("New best n = ", n, " n/p(n) = ", current_min)
#             best_n = n
#             best_min = current_min
#         # else:
#         #     print("Norm")

# its either a large prime
# or a large number made up from few other primes
for n in primes:
    current_pn = calc_pn(n, [n])
    if is_permutation(n, current_pn):
        quotient = n/current_pn
        if quotient < best_min:
            print(n)
            best_n = n
            best_min = quotient

if not best_n:
    # test combinations of two primes
    for p1 in primes:
        for p2 in primes:
            n = p1*p2
            if n > 10**7:
                break
            current_pn = calc_pn(n, [p1, p2])
            if is_permutation(n, current_pn):
                quotient = n/current_pn
                if quotient < best_min:
                    print(n)
                    best_n = n
                    best_min = quotient
print(best_n)