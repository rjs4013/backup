def dfs(si, sj):
    global ans
    visited[si][sj] = 1
    if si == stamp[M-1][0] and sj == stamp[M-1][1]:
        ans += 1
        return

    dxy = [[0,1], [1, 0], [0, -1], [-1, 0]]

    for dx, dy in dxy:
        a = si + dx
        b = sj + dy
        if 0<=a<N and 0<=b<N and visited[a][b] != 1 and arr[a][b] != 1:
            dfs(a, b)
            visited[a][b] = 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
stamp = [list(map(int, input().split())) for _ in range(M)]

visited = [[0] * N for _ in range(N)]
ans = 0
dfs(stamp[0][0] -1, stamp[0][1] -1)
print(ans)