from primes import primesfrom2to

primes = primesfrom2to(10**7)

# k_to_num = {2:4}

def get_prime_factors(num):
    factors = []
    num
    i = 0
    while i < len(primes):
        # if primes[i] > num:
        #     return factors
        if (num % primes[i]) == 0:
            factors.append(primes[i])
            num = num // primes[i]
            if num == 1:
                return factors
        else:
            i += 1
    raise "Too few primes for this number"

cache = {}

def minimal_product_sum(k):
    num = 1
    while True:
        res = try_downwards(k, 0, 1, num)
        if res:
            return res
        num += 1
        # print(num)

def try_downwards(k, prev_sum, prev_prod, max_num):
    if (k, prev_sum, prev_prod) in cache:
        return cache[(k, prev_sum, prev_prod)]


    if k == 0:
        if prev_sum == prev_prod:
            return prev_sum
        else:
            return False

    for num in range(max_num, 0, -1):
        for curr_k in range(1, k + 1):
            curr_sum = prev_sum + num * curr_k
            curr_prod = prev_prod * (num ** curr_k)
            rem = try_downwards(k - curr_k, curr_sum, curr_prod, num - 1)
            if rem:
                cache[(k, prev_sum, prev_prod)] = rem
                return rem
    
    return False

# for i in range(2,23):
#     print(i, minimal_product_sum(i))
# print(cache)
# print(len(cache))
# # print(len(set(cache)))

k_to_num = {}

def update_cache(num, factors):
    k = len(prime_factors) + num - sum(prime_factors)
    if k not in k_to_num:
        k_to_num[k] = num
    elif k_to_num[k] > num:
        k_to_num[k] = num

num = 4
min_k = 1
max_k = 12000
nums = []
while True:
    # if not num in primes:
    prime_factors = get_prime_factors(num)
    if len(prime_factors) > 1: # ignore primes
        k = len(prime_factors) + num - sum(prime_factors)
        if k > min_k:
            nums.append(num)
            print("k = ", k, " num = ", num)
            if k <= max_k:
                min_k = k
            if k >= max_k:
                # print("Prev: k = ", min_k, " num = ", nums[-2])
                # print("k = ", k, " num = ", num)
                break
    num += 1
    # if min_k > 12:
    #     break

assert len(nums) == len(set(nums))
print(nums)
print(sum(nums))
# print(sum(nums[:-1]))