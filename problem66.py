import math
import time
from sortedcontainers import SortedSet

# squares = set([x**2 for x in range(1,1000000)])

def is_square_old(x):
    # print(x)
    return ((int(math.sqrt(x))**2) == x)

def is_square(n):
    return round(n ** 0.5) ** 2 == n

def is_square_babylon(num):
  x = num // 2
  seen = set([x])
  while x * x != num:
    x = (x + (num // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def get_min_x(squares, D):
    for y_squared in squares:
        x_squared = y_squared*D + 1
        if is_square(x_squared):
            return float(x_squared)
    return False

def function_test(fun, input):
    start = time.time()
    for i in input:
        a = fun(i)
    print("Function ", fun, " took ", time.time() -start, " seconds to process ", len(input), " items")

# function_test(is_square, range(1000000,10000000))
# function_test(is_square2, range(1000000,10000000))
# exit()

best_D = None
best_x = 0

y_lower = 2
y_upper = 1000

candidates = [D for D in range(3,1001)]
while len(candidates) > 1:
    print("num candidates: ", len(candidates), " y_lower = ", y_lower, " y_upper = ", y_upper)
    new_candidates = []
    for D in candidates:
        if is_square(D):
            continue
        found = False
        for y in range(y_lower, y_upper):
            y_squared = y**2
            x_squared = D*y_squared + 1
            if is_square(x_squared):
                print("D = ", D, " x square = ", x_squared)
                found = True
                if best_x < x_squared:
                    best_x = x_squared
                    best_D = D
                break
        if not found:
            new_candidates.append(D)
    y_lower = y_upper
    y_upper *= 10
    candidates = new_candidates

print(candidates)
print(best_D)