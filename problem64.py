import math

# a0 is floor(Sqrt())

a = []

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

count_odd_period = 0
for x in range(10001):
    # print("Calc square root of ", x)

    a0 = math.floor(math.sqrt(x))

    # skip rational ones
    if a0**2 == x:
        continue

    pairs = [calc_next(x, (a0, 1, a0))]
    # print(pairs)

    while True:
        next_pair = calc_next(x, pairs[-1])
        if next_pair in pairs:
            # print(pairs)
            # print("Period of ", x, " = ", len(pairs))
            if len(pairs) % 2:
                count_odd_period += 1
            break
        else:
            pairs.append(next_pair)
            # print("Appending ", next_pair)

print("Odd periods: ", count_odd_period)