# Problem 99
import math

f = open('p099_base_exp.txt','r')
fi = f.read().split()

zahlen = [(int(zahl[0]),int(zahl[1])) for zahl in [line.split(',') for line in fi]]    # (base,exp)

exponenten = []
for zahl in zahlen:
    exponenten.append(zahl[1] * math.log(zahl[0]))


max_exp = 0
max_zeile = 0

for zeile,exp in enumerate(exponenten):
    if exp > max_exp:
        max_exp = exp
        max_zeile = zeile

print("Maximaler exponent = "+ str(max_exp))
print("Maximaler exponent zeile = " + str(max_zeile+1))
