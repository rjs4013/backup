def maze(i_start, j_start, visited, matrix):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    result = 0
    if matrix[i_start][j_start] == '3':
        return True
# 벽(1), 인덱스 초과, true
    for k in range(4):
        ni = i_start + di[k]
        nj = j_start + dj[k]

        if 0 <= ni < N and 0 <= nj < N:
            if matrix[ni][nj] != '1' and not visited[ni][nj]:
                visited[ni][nj] = True
                if maze(ni, nj, visited, matrix):
                    return True
    return False




T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    i_start = 0
    j_start = 0
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == '2':
                visited[y][x] = True
                i_start = y
                j_start = x
                break

    if maze(i_start, j_start, visited, matrix):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')