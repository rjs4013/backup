# BFS 활용
# def road(si, sj):
#     queue = []
#     visited = [[0]*N for _ in range(N)]
#     # 초기 데이터 큐 삽입, 방문표시
#     queue.append((si,sj))
#     visited[si][sj]=1
#
#     dij = [[0, 1], [1,0], [0,-1], [-1,0]]
#
#     while queue:
#         ci, cj = queue.pop(0)
#         if arr[ci][cj] == 3:
#             return visited[ci][cj]
#
#         # 4방향, 미방문, 벽이아니면 방문(queue)
#         for di, dj in dij:
#             ni, nj = ci + di, cj + dj
#             if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
#                 queue.append((ni,nj))
#                 visited[ni][nj]=1
#     return 0
#

# T = 10
# for _ in range(1, T+1):
#     test_case = int(input())
#     arr = [list(map(int, input().strip())) for _ in range(16)]
#     N = 16
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 2: continue
#             si, sj = i, j
#     ans = road(si,sj)
#     print(f'#{test_case} {ans}')

# DFS 활용
def dfs(ci, cj):
    dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for di, dj in dij:
        ni, nj = ci + di, cj + dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
            visited[ni][nj]=1
            dfs(ni,nj)


T = 10
for _ in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().strip())) for _ in range(16)]
    N = 16
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 2: continue
            si, sj = i, j
            if arr[i][j] != 3: continue
            ei, ej = i, j
    visited = [[0] * 16 for _ in range(16)]
    visited[si][sj] = 1
    dfs(si, sj)
    print(f'#{test_case} {visited[ei][ej]}')


