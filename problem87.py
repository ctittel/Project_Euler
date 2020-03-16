from primes import primesfrom2to
import math

max_sum = 50*(10**6)
primes = primesfrom2to(int(math.sqrt(max_sum)))

print("Min prime = ", primes[0])
print("Max prime = ", primes[-1])

# some caching for speedup
primes_squared = []
lim = max_sum - (2**3 + 2**4)
for p in primes:
    pp = p*p
    if pp > lim:
        break
    primes_squared.append(pp)
primes_cubed = []
lim = max_sum - (2**2 + 2**4)
for p in primes:
    ppp = p**3
    if ppp > lim:
        break
    primes_cubed.append(ppp)
primes_fourth = []
lim = max_sum - (2**2 + 2**3)
for p in primes:
    pppp = p**4
    if pppp > lim:
        break
    primes_fourth.append(pppp)

print(len(primes_squared))
print(len(primes_cubed))
print(len(primes_fourth))


count = 0

print("First elements: ", primes_squared[0], primes_cubed[0], primes_fourth[0])
print("Last elements: ", primes_squared[-1], primes_cubed[-1], primes_fourth[-1])

nums = set()

for p2 in primes_squared:
    for p3 in primes_cubed:
        for p4 in primes_fourth:
            n = p2 + p3 + p4
            if n >= max_sum:
                break
            if n not in nums:
                count += 1
                nums.add(n)

print(count)