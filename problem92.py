zahlen = []


def sum_squares(x):
    sum = 0
    while (x != 0):
        digit = x % 10
        sum += digit**2
        x = x//10
    return sum

