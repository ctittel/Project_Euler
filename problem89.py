with open('p089_roman.txt') as f:
    roman = f.read()

roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
def roman_to_dec(roman):
    nums = [roman_to_int[i] for i in roman]
    nums_start = nums.copy()
    prev_len = 0
    while prev_len != len(nums):
        prev_len = len(nums)
        for i in range(0, len(nums) - 1):
            if nums[i+1] > nums[i]:
                nums[i+1] -= nums[i]
                nums[i] = 0
        nums = [i for i in nums if i > 0]
    return sum(nums)

# int_to_roman = [(v,k) for k,v in roman_to_int]
# int_to_roman.sort(key=lambda x: x[0])
# int_to_roman.reverse()

# [(1000, 'M'), (900, 'CM'), (800, 'CCM'), (700, 'DCC'), (600, 'DC'), (500, 'C'), (400, 'CD'), (300, 'CCD'), (200, 'CC'), (100, 'C')]
vals_and_counts = [(10, 1), (9, 2), (8, 4), (7, 3), (6,2), (5,1), (4,2), (3,3), (2,2), (1,1)]

def ideal_roman_count(num):
    total_count = 0
    size = 100
    while size >= 1:
        for val, count in vals_and_counts:
            if val in [1,2,3,4,5,6,7,8,9]:
                if num // (size * val) > 1:
                    raise "shouldn't happen"
            total_count += count * (num // (size * val))
            num = num % (size * val)
        size /= 10
    if num != 0:
        raise "ff"
    return int(total_count)


def calc_diff(roman):
    dec = roman_to_dec(roman)
    optimal_count = ideal_roman_count(dec)
    diff = len(roman) - optimal_count
    print(roman, ' = ', dec, ' optimal count = ', optimal_count, ' diff = ', diff)
    if diff < 0:
        raise "This should not happen"
    return diff


count = 0
roman = roman.split('\n')
assert len(roman) == 1000
for r in roman:
    count += calc_diff(r)
print(count)

print(calc_diff('XIIIIII'))