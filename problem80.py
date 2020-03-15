import math

def fraction_to_decimal_digits(num, denum, count_digits):
    digits = []

    while num > 10*denum:
        denum *= 10

    while len(digits) < count_digits:
        digits.append(num // denum)
        num = num % denum
        num = 10 * num
    return digits

def num_plus_fraction(a, frac):
    return (frac[1]*a+frac[0], frac[1])

def num_div_fraction(a, frac):
    return (frac[1]*a, frac[0])

def get_root_fraction(x, level):
    num = x-1
    denum = 2
    while level > 0:
        num, denum = num_plus_fraction(2, (num, denum))
        num, denum = num_div_fraction(x-1, (num, denum))
        level -= 1
    return num_plus_fraction(1, (num, denum))




def test():
    num,denum = get_root_fraction(2, 1000)
    a = fraction_to_decimal_digits(num, denum,100)
    assert len(a) == 100
    print(sum(a))
    print(a)
    print(''.join([str(i) for i in a]))
    assert sum(a) == 475
    # print(len(a))

test()

s = 0
for i in range(1,101):
    if int(math.sqrt(i)) == math.sqrt(i):
        continue
    num, denum = get_root_fraction(i, 10000)
    current_s = sum(fraction_to_decimal_digits(num, denum, 100))
    s += current_s
    print("Number = ", i, " Sum = ", current_s)

print(s)
