sorted_num_to_count = {}
sorted_num_to_smallest = {}

i = 2
while True:
    cube = i**3
    a = sorted(str(cube))
    # if '0' in a:
    #     a.remove('0')
    a = ''.join(a)

    if a not in sorted_num_to_count:
        sorted_num_to_count[a] = 1
        sorted_num_to_smallest[a] = cube
    else:
        sorted_num_to_count[a] += 1
        if sorted_num_to_count[a] >= 5:
            print(sorted_num_to_smallest[a])
            break

    i += 1