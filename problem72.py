from primes import primesfrom2to

primes = primesfrom2to(10**7)

def calc_pn(n, prime_factors):
    f = n
    for p in prime_factors:
        f *= (1- (1/p))
    return int(f)

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


    # while 
    #     yield [primes[p_id]] * k
    #     for n in get_factors(p_id+1, product_limit, current_product):
    #         yield n + [primes[p_id]] * k
    #     k += 1
    #     current_product = prev_product + (primes[p_id]**k)
    # return

s = 0
for product, prime_factors  in get_factors(0, 10**6, 1):
    # print(n)
    # if not i%100:
    #     print(i)
    s += calc_pn(product, prime_factors)
    # print(product, prime_factors, )
    # print(n, calc_pn())
    # if i > 100:
    #     break
print("DONE, SUM: ", s)