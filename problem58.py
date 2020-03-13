from primes import primesfrom2to
import time
import numpy as np

def numbers_on_diagonals(side_length):
    nums = [1]
    for s in range(3, side_length, 2):
        for i in range(4):
            nums.append(nums[-1]+s-1)
    return nums

# print(numbers_on_diagonals(7))

s = time.time()
primes = primesfrom2to(1000000000)
p_ind = 0
# primes = np.array(primes)
print("Calculated ", len(primes), " primes in ", time.time() - s, " seconds!")


def is_prime(num, next_num = None):
    global primes
    global p_ind
    i = p_ind
    while i < len(primes):
        if primes[i] >= num:
            break
        else:
            i += 1
    # for i, p in enumerate(primes):
    #     if p >= num:
    #         break
    # i = np.argmax(n >= primes)

    if i >= len(primes):
        raise "ERROR too few primes"

    res = (primes[i] == num)
    # primes = primes[i:]
    if not next_num:
        p_ind = i
    elif primes[i] < next_num:
        p_ind = i
    return res


total_nums = 5
total_primes = 3
side_length = 3
largest_num = 9
while True:
    side_length += 2
    new_nums = [largest_num + i*(side_length-1) for i in range(1,5)]
    largest_num = new_nums[-1]
    total_nums += 4
    for n in new_nums:
        # i = np.argwhere()

        # for i, p in enumerate(primes):
        #     if p >= n:
        #         break
        # i = np.argmax(n >= primes)
        if is_prime(n):
            total_primes += 1
        # primes = primes[i:]

    p = total_primes/total_nums

    if not side_length % 11:
        print("side length ", side_length, " total_nums=",total_nums, "total_primes=", total_primes, "percentage=",p)
    if p <= 0.1:
        print("side length ", side_length, " total_nums=",total_nums, "total_primes=", total_primes, "percentage=",p)
        break

    if largest_num > primes[-1]:
        raise "Largest spiral number is " + str(largest_num) + ", the largest calculated prime is " + str(primes[-1]) + "!!! NEED MORE PRIMES!"