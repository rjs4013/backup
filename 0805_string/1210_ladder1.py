def ladder(N, start_i, start_j, visited):
    if start_i == 0:
        return start_j
    visited[start_i][start_j] = True
    di = [0, 0, -1]
    dj = [1, -1, 0]
    for k in range(3):
        ni = start_i + di[k]
        nj = start_j + dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and visited[ni][nj] == False:
            return ladder(N, ni, nj, visited)

    return None





T = 10
for _ in range(1, T+1):
    test_case = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    start_i = 99
    start_j = 0
    for j in range(N):
        if arr[N-1][j] != 2:
            continue
        start_j = j
        break
    result = ladder(N, start_i, start_j, visited)

    print(f"#{test_case} {result}")