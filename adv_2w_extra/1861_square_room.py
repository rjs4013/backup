'''
방에 숫자가 적혀있음(모든 방에 대해 서로 다름)
상하좌우 방으로 이동가능
이동 규칙 -> 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야함.
출력 : 가장 많은 방을 이동할 수 있는 숫자가 적힌 방 번호 + 최대 몇 개의 방?
IF 최대 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것 출력
'''
def dfs(si, sj):
    global cnt
    if memo[si][sj] != -1:
        return memo[si][sj]

    dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited[si][sj] = 1
    max_count = 1

    for di, dj in dij:
        ni = si + di
        nj = sj + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] - arr[si][sj] == 1:
            max_count = max(max_count, dfs(ni, nj) + 1)

    visited[si][sj] = 0
    memo[si][sj] = max_count
    return max_count


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    ans = float('inf')
    visited = [[0] * N for _ in range(N)]
    memo = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp_cnt = dfs(i, j)
            if temp_cnt > cnt:
                cnt = temp_cnt
                ans = arr[i][j]
            elif temp_cnt == cnt:
                ans = min(ans, arr[i][j])

    print(f"#{test_case} {ans} {cnt}")


