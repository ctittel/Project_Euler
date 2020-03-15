from primes import primesfrom2to

primes = primesfrom2to(10**7)

def get_factors(p_id, product_limit, prev_product):
    # yield []
    for current_p_id in range(p_id, len(primes) + 1):
        if prev_product * primes[current_p_id] > product_limit:
            return
        
        k = 1
        current_product = prev_product * (primes[current_p_id]**k)
        while current_product <= product_limit:
            yield current_product, [primes[current_p_id]] # *k outcommented because we only need unique factors
            for next_product, n in get_factors(current_p_id+1, product_limit, current_product):
                yield next_product, [primes[current_p_id]] + n # *k outcommented because we only need unique factors
            k += 1
            current_product = prev_product * (primes[current_p_id]**k)

def count_possible_nominators(d, d_factors, p_id, prev_product):
    min_n = d/3
    max_n = d/2

    count = 0
    for current_p_id in range(p_id, len(primes) + 1):
        p = primes[current_p_id]
        if p in d_factors:
            continue
        if prev_product * p > max_n:
            return count

        current_product = prev_product * p
        k = 1
        while current_product < max_n:
            if current_product > min_n:
                count += 1
            count += count_possible_nominators(d, d_factors, current_p_id+1, current_product)
            k += 1
            current_product = prev_product * (p ** k)

count = 0
i = 0
for d, d_factors in get_factors(0, 12000, 1):
    # print(d)
    count += count_possible_nominators(d, set(d_factors), 0, 1)
    if not i%100:
        print("#", i, " d = ", d, " current count = ", count)
    i += 1

print("Total count = ", count)

# not optimized but works