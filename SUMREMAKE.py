'''
3 3
1 2 3
4 5 6
9 8 7
'''
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    print(arr[0:M][0])
    current_sum = 0
    s_max = current_sum
    s_min = current_sum
    m_len = 0
    a = []
    for i in range(N-M-1):
        current_sum += arr[i][0]
        if m_len < len(arr[i]):
            m_len = len(arr[i])

    for v in range(m_len):
        for k in range(1, N-M+1):
            current_sum = current_sum - arr[k-1][v] + arr[k+M-1][v]
            if current_sum > s_max: s_max = current_sum
            elif current_sum < s_min: s_min = current_sum
        for j in range(N):
            if len(arr[j]) == v+1:
                arr[j][-1] = -1
