from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(x, y):
    queue = deque([(x,y)])
    farm[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N and farm[nx][ny] == 1:
                queue.append((nx,ny))
                farm[nx][ny] = 0

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
            if farm[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)