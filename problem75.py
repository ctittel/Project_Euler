from primes import primesfrom2to
import math
import time

primes = primesfrom2to(10**7)

# 1. Find all primitive pytagorean triples
# 2. Check if their line lengths are unique - if not remove them
# 3. scale them up and add to the sum

def generate_prime_products(p_id, prev_product, upper_product_limit, lower_product_limit, exception_primes=None):
    # yield []
    global primes

    if prev_product == 1:
        yield 1, []

    for current_p_id in range(p_id, len(primes) + 1):
        if prev_product * primes[current_p_id] > upper_product_limit:
            return
        
        if exception_primes and primes[current_p_id] in exception_primes:
            continue

        k = 1
        current_product = prev_product * (primes[current_p_id]**k)
        while current_product <= upper_product_limit:
            if current_product > lower_product_limit:
                yield current_product, [primes[current_p_id]]*k
            for next_product, n in generate_prime_products(current_p_id+1, current_product, upper_product_limit, lower_product_limit, exception_primes):
                yield next_product, [primes[current_p_id]]*k + n
            k += 1
            current_product = prev_product * (primes[current_p_id]**k)


start = time.time()
triples = []

L_max = 1500000

c_max = L_max * 0.5
m_max = math.floor(math.sqrt(c_max - 1))
for m, m_primes in generate_prime_products(0, 1, m_max, 0.0, None):
    n_max = math.floor(math.sqrt(c_max - m**2))
    if n_max > m:
        n_max = m
    for n, n_primes in generate_prime_products(0, 1, n_max, 0.0, m_primes):
        # if not n%1000:

        if m % 2 and n % 2:
            continue

        a = m**2-n**2
        b=2*m*n
        c=m**2+n**2

        t = (a,b,c)
        if a > b:
            t = (b,a,c)

        # if c > 100 and c <= 300:
        if a+b+c <= L_max:
            triples.append(t)
            # print(t)
triples = set(triples)
print("Found " , len(triples), " primitive triplets in ", time.time() - start, " seconds")
lens = []

single_lens = set()
repeated_lens = set()

for t in triples:
    l = sum(t)
    for k in range(1, math.floor(L_max / l) + 1):
        if l*k in single_lens:
            repeated_lens.add(l*k)
        else:
            single_lens.add(l*k)

print(len(single_lens) - len(repeated_lens))
# count = 0
# for l in lens:
#     if lens.count(l) == 1:
#         count += 1

# print(count)
# # print(triples)