#Problem 85

rects = [0,0,3]

def calc_rects(anz_rects):
    min_rects = rects[2]
    rects_index = 2
    while anz_rects >= (min_rects * rects[-2]):
        rects_index += 1
        rects.append(rects[-1] + rects_index)
    return rects_index


ges_rects = 2*(10**6)
max_index = calc_rects(ges_rects)
last_x = max_index
min_diff = ges_rects
min_coords = (2,2)

diff = ges_rects
last_diff = ges_rects
x = max_index

for y in range(2,max_index//2):
    diff = ges_rects
    while diff >= 0:
        x -= 1
        last_diff = diff
        diff = rects[y]*rects[x] - ges_rects
    if abs(diff) < min_diff:
        min_diff = abs(diff)
        min_coords = (x,y)
    x += 1
    if last_diff < min_diff:
        min_diff = last_diff
        min_coords = (x,y)
    print("Y = " + str(y) + " diff1 = " + str(last_diff) + " diff2 = " + str(diff))

print("Minimale Koordinaten: " + str(min_coords))
print("Minimale Differenz: " + str(min_diff))
print("Fläche dafür: " + str(min_coords[0]*min_coords[1]))
