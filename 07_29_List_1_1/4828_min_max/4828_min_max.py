T = int(input())
for x in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
    for i in range(1, N):
        if min_v > arr[i]:
            min_v = arr[i]
    print(f'#{x+1} {max_v - min_v}')