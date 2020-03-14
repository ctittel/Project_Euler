import math
import time

# squares = set([x**2 for x in range(1,1000000)])

def is_square_old(x):
    # print(x)
    return ((int(math.sqrt(x))**2) == x)

def is_square_babylon(num):
  x = num // 2
  seen = set([x])
  while x * x != num:
    x = (x + (num // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True
  
all_squares = set([i**2 for i in range(2, 10000000)])

def is_square(x):
    global all_squares
    return x in all_squares

def get_min_x(squares, D):
    for y_squared in squares:
        x_squared = y_squared*D + 1
        if is_square(x_squared):
            return float(x_squared)
    return False


# for D in range(3, 1001):
#     # skip if D is square
#     if is_square(D):
#         continue

#     print(D, get_min_x(D))
#     # print(get_min_x(D))

best_D = None
best_x = 0

candidates = [D for D in range(3,1001)]
squares_min = 1
squares_max = 10
while len(candidates) > 1:
    print("Starting new loop with squares min = ", squares_min, " squares max = ", squares_max, " num candidates = ", len(candidates))
    new_candidates = []
    squares = [x**2 for x in range(squares_min,squares_max)]
    print("... calculated squares list")
    for D in candidates:
        x = get_min_x(squares, D)
        if not x:
            new_candidates.append(D)
        elif x > best_x:
            best_x = x
            best_D = D
            print("..... new highest x = ", best_x, " for D = ", best_D)
    candidates = new_candidates
    squares_min *= 10
    squares_max *= 10
    # print("suqares min = ", squares_min, " squares max = ", squares_max, " len candidates = ", len(candidates))
    print("... loop done")

print("highest x = ", best_x, " for D = ", best_D)
print("Candidates = ", candidates)