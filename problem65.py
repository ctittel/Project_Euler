import math

def num_plus_frac(a,frac):
    """ Input: a + (b/c)
        Output: (num, denum) """
    return (a*frac[1] + frac[0], frac[1])

num = 100

convergents = []
for i in range(num):
    k = 1
    if (i % 3) == 1:
        k = 2 * (1 + (i//3))
    convergents.append(k)

s = (0, 1)
for c in convergents[::-1]:
    # print(c)
    s = num_plus_frac(c, s[::-1])

s = num_plus_frac(2, s[::-1])
print("Fraction #", num, ": ", s[0], "/", s[1])
print("Digit sum of ", s[0], " = ", sum([int(x) for x in str(s[0])]))