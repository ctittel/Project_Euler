from primes import primesfrom2to

primes = primesfrom2to(1000000)
# print(primes)

# ignore all numbers which are
#   - prime
#   - are simple multiples of a prime

def primes_smaller_than(x):
    print(primesfrom2to(x))
    return len(primesfrom2to(x)) + 1

max_n = 1000000
n = 1
i = 0
while n*primes[i] <= max_n:
    n *= primes[i]
    i += 1

num_relatively_prime = primes_smaller_than(n)
print("n = ", n, " p(n) = ", num_relatively_prime, " n/p(n) = ", n/num_relatively_prime)