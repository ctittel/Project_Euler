nomi = [1]
denomi = [2]

for i in range(999):
    d = denomi[-1]
    n = nomi[-1]
    nomi.append(d)
    denomi.append(n + d * 2)

assert len(nomi) == 1000
assert len(denomi) == 1000

count = 0
for n, d in zip(nomi,denomi):
    if len(str(n+d)) > len(str(d)):
        count += 1
print(count)