def sheep(N):
    k = 1
    all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    fuel = []
    l = 0
    numdiv = N
    while l < 10:
        numdiv = k * N
        w = list(map(int, str(numdiv)))
        for i in all_numbers:
            for j in w:
                if i == j and j not in fuel:
                    fuel.append(j)
        k += 1
        l = len(fuel)
    return numdiv



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case} {sheep(N)}')