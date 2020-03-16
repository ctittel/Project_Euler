max_k = 12000

cache = {}
def update_cache(prev_prod, prev_sum, prod_factors, min_num):
    global cache
    k = prod_factors - prev_sum + prev_prod
    if k <= max_k:
        if k not in cache:
            cache[k] = prev_prod
        else:
            if cache[k] > prev_prod:
                cache[k] = prev_prod
        for i in range(min_num, max_k//prev_prod * 2 + 1):
            update_cache(prev_prod*i, prev_sum + i, prod_factors + 1, i)

update_cache(1, 1, 1, 2)
print(cache)
print(sum(set([v for k,v in cache.items()])) - 1) # - 1 because the 1 is in my set