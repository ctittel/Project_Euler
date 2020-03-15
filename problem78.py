import math
# n     number of coins
# p(n)  number of possible seperations
# n for which p(n) = k*10**6

# Ramanuja's conjuncture
# k = 1

prev_to_sign = []

for k in range(-10000,10000):
    if k==0:
        continue
    sign = int(-1*(-1)**k)
    n = int((3*(k**2)+k)*0.5)
    prev_to_sign.append((n,sign))

prev_to_sign.sort(key=lambda x: x[0])
# for p, s in prev_to_sign:
#     if s == -1:
#         print("-p(n-",p,")")
#     else:
#         print("+p(n-",p,")")

previous_pn = {0:1, 1:1}

# print(prev_to_sign[:10])

def pn_recursive(n):
    global previous_pn
    s = 0
    for prev_n, sign in prev_to_sign:
        i = n - prev_n
        if i < 0:
            if n not in previous_pn:
                previous_pn[n] = s
            return s
        else:
            s += sign*previous_pn[i]

for i in range(2, 10**6):
    pn = pn_recursive(i)
    if not pn % 10**6:
        print(i, pn_recursive(i))
        break

# for i, n in enumerate(range(1,10**7)):
#     pn = (1/(4*n*math.sqrt(3)))*math.exp(math.pi*math.sqrt(2*n/3))
#     pn = int(pn)
#     if not i%100:
#         print("p(",n,") =",pn)
#     if not pn % 10**6:
#         print("DONE, n =",n, " pn = ",pn)
#         break

# print(prev_to_sign)