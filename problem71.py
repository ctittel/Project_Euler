from primes import primesfrom2to

primes = primesfrom2to(10**6)

left = 2/5
right = 3/7

best_n = 2
best_d = 5
for d in range(2, 10**6+1):
    for n in range(int(left*d)-1, int(right*d)+1):
        q = n/d
        if q >= right:
            # print(n, "/", d, "=", q, " >= ", right)
            continue
        if q > left:
            left = q
            best_n = n
            best_d = d
            # print(n, "/", d, "=", q, " > ", left, "GOOD")
print("Best n = ", best_n, " best d = ", best_d)