T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    current_sum = sum(arr[:M])
    max_sum = current_sum
    min_sum = current_sum

    for i in range(1, N-M+1):
        current_sum = current_sum - arr[i-1] + arr[i+M-1]
        if current_sum > max_sum: max_sum = current_sum
        elif current_sum < min_sum: min_sum = current_sum

    print(f'#{test_case} {max_sum-min_sum}')