def fac(n):
    s = 1.0
    for i in range(1,n+1):
        s*=i
    # print("Fact of ", n, ": ", s)
    return s

def combs(n,r):
    return fac(n) / (fac(r) * fac(n-r))

count = 0
for n in range(1,101):
    upper = 1
    lower = 100
    for r in range(n, 0, -1):
        if combs(n,r) >= 1000000:
            upper = r
            break
    for r in range(1, n+1):
        if combs(n,r) >= 1000000:
            lower = r
            break
    if lower > upper:
        print("ERROR")
    else:
        count += upper - lower + 1

print(count)