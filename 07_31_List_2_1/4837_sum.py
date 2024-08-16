T = int(input())
for x in range(T):
    N, K = list(map(int,input().split()))
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = len(arr)
    subset_cnt = 2**n

    subsets = []
    for i in range(subset_cnt):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        subsets.append(subset)
    acount = 0
    answer = 0
    for o in range(len(subsets)):
        if sum(subsets[o]) == K and len(subsets[o]) == N:
            acount += 1
    print(f'#{x+1} {acount}')