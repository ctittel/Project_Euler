def list_of_combinations(num1, num2):
    l = []
    l.append(num1+num2)
    l.append(num1*num2)
    l.append(num1-num2)
    l.append(num2-num1)
    if num2 != 0:
        l.append(num1/num2)
    if num1 != 0:
        l.append(num2/num1)
    return l

def list_of_all_combinations(liste):
    ret = []
    for e1 in liste:
        l2 = list(liste)
        l2.remove(e1)
        for e2 in l2:
            l3 = list(l2)
            l3.remove(e2)
            for e3 in l3:
                l4 = list(l3)
                l4.remove(e3)
                e4 = l4[0]
                c1 = list_of_combinations(e1,e2)
                c2 = list_of_combinations(e2,e3)
                for a1 in c1:
                    for a2 in c2:
                        ret += list_of_combinations(a1,a2)
                        
    return ret

def cleanup_list(li):
    res = []
    for el in li:
        if is_valid(el):
            res.append(el)
    return res

def is_valid(num):
    if (num % 1) == 0:
        if num >= 0:
            return True
    else:
        return False

def set_len(li):
    nums = set(li)
    i = 0
    while (i+1) in nums:
        i += 1
    return i

max_len = 0
max_nums = 0

for a in range(1,7):
    for b in range(a+1,8):
        for c in range(b+1,9):
            for d in range(c+1,10):
                print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + ", d = " + str(d))
                clean_list = cleanup_list(list_of_all_combinations([a,b,c,d]))
                combo_len = set_len(clean_list)
                print(combo_len)
                if combo_len > max_len:
                    max_len = combo_len
                    max_nums = str(a) + str(b) + str(c) + str(d)
                    print("NEW MAX LENGTH")

print("für 1 2 3 4")
l = list_of_all_combinations([1,2,3,4])
lc = cleanup_list(l)
print(set(l))
print(set(lc))
print(len(lc))
print(set_len(lc))

print ("MAX LENGth:")
print(max_len)
print("ZAHLEN: " + max_nums)