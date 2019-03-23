import sys

sys.setrecursionlimit(1500)
def fact(nu):
    loes = 1
    while nu > 1:
        loes *= nu
        nu -= 1
    return loes

factors = [fact(x) for x in range(10)]
print(factors)

def factorial(nu):
    summe = 0
    while nu:
        summe += factors[nu % 10]
        nu = nu // 10
    return summe

nummern = [0 for x in range(10**6)]

loop_nums = [145,169,871,872]
for num in [169,363601,1454]:
    nummern[num] = 3
for num in [871,45361]:
    nummern[num] = 2
for num in [872,45362]:
    nummern[num] = 2
nummern[145] = 1

last_num = 0
def chain_lens(num):
    global last_num
    if last_num == num:
        return 0
    last_num = num
    if num < 10**6:
        if not nummern[num]:
            nummern[num] = chain_lens(factorial(num)) + 1
        return nummern[num]
    else:
        return chain_lens(factorial(num)) + 1


for nu in range(1,10**6):
    last_num = 0
    if chain_lens(nu) in [0,1,2,59,60,61]:
        print("Die Zahl " + str(nu) + " hat so viele Terme: " + str(nummern[nu]))

loesungen = [x for x in nummern if x >= 60]
print(loesungen)
print("Anzahl = " + str(len(loesungen)))
