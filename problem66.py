import math

def num_plus_frac(a,frac):
    """ Input: a + (b/c)
        Output: (num, denum) """
    return (a*frac[1] + frac[0], frac[1])

def num_div_frac(a,frac):
    """ a / (b/c) """
    return (frac[1] * a, frac[0])

def calc_next(x, prev_pair):
    # print('calc_next INPUT ', prev_pair)
    b_prev = prev_pair[1]
    c_prev = prev_pair[2]

    if not b_prev:
        return prev_pair

    b = int((x - (c_prev**2))/b_prev)

    c = math.floor(math.sqrt(x))
    a = 0

    while b:
        s = c_prev + c
        # print("s = ",s, " b = ", b)
        if ((s//b) == (s/b)):
            a = s//b
            break
        c -= 1

    assert a >= 0
    assert b >= 0
    assert c >= 0
    # print('calc_next OUTPUT ', (a, b, c))
    return (a, b, c)

def calc_solution(D):
    """ x^2 - D * y^2 = 1 - return (x,y) that are integers """
    a0 = math.floor(math.sqrt(D))

    # skip rational ones
    if a0**2 == D:
        return None

    pairs = [calc_next(D, (a0, 1, a0))]
    num = 1
    denum = pairs[-1][0]

    x = (num+a0*denum)
    y = denum

    while x**2 - D * y**2 != 1:
        pairs.append(calc_next(D, pairs[-1]))
        next_a = pairs[-1][0]

        num, denum = num_div_frac(1, num_plus_frac(next_a, (num, denum)))

        x = (num+a0*denum)
        y = denum
    return x,y


def is_square(x):
    return int(math.sqrt(x))**2 == x


best_x = 0
best_D = None

for D in range(2,1001):
    print("Calculating D = ", D)
    if is_square(D):
        continue

    x, y = calc_solution(D)

    print("D = ", D, "   x = ", x)
    if x > best_x:
        best_x = x
        best_D = D

print("best_x = ", best_x, " for best_D = ", best_D)