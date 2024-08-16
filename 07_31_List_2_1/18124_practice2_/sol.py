T = int(input())
for test_case in range(1,T+1):
    arr = list(map(int,input().split()))
    N = len(arr)
    subset_count = 2 ** N

    subsets = []
    for i in range(1, subset_count):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(arr[j])
        subsets.append(subset)

    x = 0
    while x < len(subsets):
        if sum(subsets[x]) != 0:
            x += 1
        else:
            print(f'#{test_case} 1')
            break
    else:
        print(f'#{test_case} 0')








