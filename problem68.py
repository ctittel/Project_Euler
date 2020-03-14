from itertools import permutations

vals = [9,8,7,6,5,4,3,2,1,10]

def recurse(level, remaining_vals, outer=None, inner=None, req_sum=None):
    if level == 0:
        collected_results = []
        assert len(remaining_vals) == 10
        for a1, a2, a3 in permutations(remaining_vals[::-1], 3):
            outer = [a1]
            inner = [a2, a3]
            s = a1+a2+a3
            r = remaining_vals.copy()
            r.remove(a1)
            r.remove(a2)
            r.remove(a3)
            assert len(r) == 7
            result = recurse(1, r, outer, inner, s)
            if result:
                for res in result:
                    rr = [[a1, a2, a3]] + res
                    # print("level ", level, " returning ", res)
                    if len(''.join(["".join([str(j) for j in i]) for i in rr])) == 16:
                        collected_results.append(rr)
        return collected_results
    elif level == 4:
        assert len(outer) == 4
        assert len(inner) == 5
        assert len(remaining_vals) == 1
        a1 = remaining_vals[-1]
        a2 = inner[4]
        a3 = inner[0]
        if a1+a2+a3 == req_sum:
            res = [[[a1, a2, a3]]]
            # print("level 4 returning = ", res)
            return res
        else:
            return False
    else:
        # print("test")
        if not len(remaining_vals) == (10 - 3 - (level - 1)*2):
            print("remaining value count: ", len(remaining_vals), ": ", remaining_vals, " should be = ", (10 - 3 - (level - 1)*2))
        a2 = inner[-1]
        collected_results = []
        for a1, a3 in permutations(remaining_vals, 2):
            if a1+a2+a3 == req_sum:
                r = remaining_vals.copy()
                r.remove(a1)
                r.remove(a3)
                result = recurse(level+1, r, outer+[a1], inner+[a3], req_sum)
                if result:
                    for res in result:
                        collected_results.append([[a1,a2,a3]] + res)
                    # res = [[a1,a2,a3]] + result
                    # print("level ", level, " returning ", res)
                    # return res
        return collected_results

def join_gon_ring(nums):
    lowest = 10
    lowest_i = None
    for i, n in enumerate(nums):
        if n[0] <= lowest:
            lowest = n[0]
            lowest_i = i
    nums = nums[lowest_i:] + nums[:lowest_i]
    s = "".join(["".join([str(i) for i in j]) for j in nums])
    return int(s)

results = recurse(0, vals)
print(results)
results = [join_gon_ring(r) for r in results]
print(results)
print(max(results))