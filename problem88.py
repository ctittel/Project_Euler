# k_to_num = {2:4}

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

for i in range(2,23):
    print(i, minimal_product_sum(i))
print(cache)
print(len(cache))
# print(len(set(cache)))