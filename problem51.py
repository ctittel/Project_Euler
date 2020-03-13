from primes import sundaram3
import time

min_brothers = 8
max_fails = 10 - min_brothers

primes = [str(i) for i in sundaram3(1000000)]
# print(primes)

start = time.time()

for p in primes:
    for num in p:
        count = 0
        fails = 0
        for replace_num in range(0,10):
            # if replace_num == num:
            #     continue
            if p.replace(num, str(replace_num)) in primes:
                count += 1
            else:
                fails += 1
                if fails > max_fails:
                    break
        if count >= min_brothers:
            print("Replacing ", num, " in ", p, " = ", count)
            print(time.time() - start)
            break

# 183 seconds
# can be improved with better data structures and search