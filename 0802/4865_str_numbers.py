T = int(input())
for t in range(1,T+1):
    n_dict = {}
    a = list(input())
    b = list(input())
    for sub_a in a:
        n_dict[sub_a] = 0
        for sub_b in b:
            if sub_a == sub_b:
                n_dict[sub_a] += 1
    max_val = 0
    for x,y in n_dict.items():
        if max_val < y:
            max_val = y
    print(max_val)
