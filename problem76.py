cache = dict()

def num_sums(remaining_sum, max_num = None):
    global cache
    count = 1 # accounting for num = 1 in the loop
    if max_num == None:
        max_num = remaining_sum - 1
        # count = 0

    if remaining_sum == 0 or max_num == 1:
        return 1

    if max_num == 0:
        raise "this shouldn't happen"

    if (remaining_sum, max_num) in cache:
        return cache[(remaining_sum, max_num)]

    for num in range(max_num, 1, -1):
        k = 1
        current_sum = remaining_sum - num
        while current_sum >= 0:
            count += num_sums(current_sum, num-1)
            k += 1
            current_sum = remaining_sum - k * num

    cache[(remaining_sum, max_num)] = count
    return count

assert num_sums(6) == 10
assert num_sums(5) == 6
assert num_sums(4) == 4
assert num_sums(3) == 2
assert num_sums(2) == 1

print(num_sums(100))