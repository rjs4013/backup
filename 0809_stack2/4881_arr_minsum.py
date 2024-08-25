def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, sm + arr[n][j])
            visited[j] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    ans = float('inf')
    dfs(0, 0)

    print(ans)




















# def dfs(n, sm):
#     global ans
#     if ans <= sm:
#         return
#
#     if n==N:
#         ans = min(ans, sm)
#         return
#
#     for j in range(N):
#         if visited[j] == 0: # 사용되지 않은 숫자
#             visited[j] = 1
#             dfs(n+1, sm + arr[n][j]) # 현재 열 값을 sm에 더하여 재귀 호출
#             visited[j] = 0 # return 이후 돌아와서 0으로 visited 초기화 -> 이전 행의 다음 열에서 올 경우 쓰일 수 있음
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [0] * N
#     ans = 100
#     dfs(0,0)
#
#     print(f'#{test_case} {ans}')

    # col_visited = [0]*N
    # list_sum = []
    # for i in range(N):
    #     num_min = float('inf')
    #     for j in range(N):
    #         if arr[i][j] < num_min and col_visited[j] == 0:
    #             num_min = arr[i][j]
    #     list_sum.append(num_min)
    #     for k,v in enumerate(arr[i]):
    #         if v == num_min:
    #             col_visited[k] = 1
    #             break
    #
    #
    # answer = sum(list_sum)
    # print(f'#{test_case} {answer}')
