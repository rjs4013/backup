def dfs(x, y):
    # 범위 벗어나는 경우 즉시 종료
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    # 방문 하지 않은 배추밭이라면
    if farm[x][y] == 1:
        # 방문 처리 한다음
        farm[x][y] = 0
        # 상하좌우 위치 모두 재귀호출
        # 단순 방문 처리 목적
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


T = int(input())
for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]

    # 배추 심기
    for i in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1

    # 모든 위치에 대하여 탐색 수행
    ans = 0
    for i in range(M):
        for j in range(N):
            if dfs(i,j) == True:
                ans += 1

    print(ans)