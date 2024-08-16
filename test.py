def maze(i_start, j_start, visited, matrix):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 목적지 도달 여부를 추적할 변수
    if matrix[i_start][j_start] == '3':
        return True

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
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 시작 위치 찾기
    i_start = j_start = -1
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == '2':
                i_start = y
                j_start = x
                visited[i_start][j_start] = True
                break
        if i_start != -1:
            break

    if maze(i_start, j_start, visited, matrix):
        print(1)
    else:
        print(0)
