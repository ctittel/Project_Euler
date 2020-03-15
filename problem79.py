with open('p079_keylog.txt') as f:
    keylog = f.read()
keylog = keylog.split('\n')
keylog = keylog[:-1]
keylog = set(keylog)

pairs = []
for a,b,c in [tuple(s) for s in keylog]:
    pairs.append((a,b))
    pairs.append((b,c))

pairs = set(pairs)

# prio = {}

# # assumption: each number just once

for b in pairs:
    if b[::-1] in pairs:
        print("REPEATED DIGIT REQUIRED")

def build_key(pairs):
    if len(pairs) == 0:
        return ""

    ids = set([a for a,b in pairs] + [b for a,b in pairs])
    count_first = {i:0 for i in ids}
    count_last = {i:0 for i in ids}
    for a,b in pairs:
        count_first[a] += 1
        count_last[b] += 1

    my_first = None
    my_last = None
    for i, v in count_first.items():
        if v == 0:
            my_last = i
            break
    for i, v in count_last.items():
        if v == 0:
            my_first = i
            break

    new_pairs = pairs.copy()
    for p in pairs:
        if p[0] == my_first or p[1] == my_last:
            new_pairs.remove(p)

    return my_first + build_key(new_pairs) + my_last

print(build_key(pairs))