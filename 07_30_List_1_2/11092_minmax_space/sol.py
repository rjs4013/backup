T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_a = float('inf')
    max_a = float('-inf')
    min_idx = 0
    max_idx = 0
    for i in range(N):
        if arr[i] < min_a:
            min_a = arr[i]
            min_idx = i
        if arr[i] >= max_a:
            max_a = arr[i]
            max_idx = i
    print(f'#{test_case} {max_idx - min_idx}')