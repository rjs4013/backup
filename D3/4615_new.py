T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    turn = [list(map(int, input().split())) for _ in range(M)]
    table = [[0] * N for p in range(N)]
    a = N // 2 - 1
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    table[a][a], table[a + 1][a + 1] = 2, 2     # 중앙 백돌
    table[a][a + 1], table[a + 1][a] = 1, 1     # 중앙 흑돌

    for x in turn:
        row, col, color = x[1] - 1, x[0] - 1, x[2]      # 자기 턴에 돌 놓는 인덱스 위치 찾기(열, 행)
        table[row][col] = color                         # 보드에 흑, 백 놓기

        for k in range(8):
            ni, nj = row + di[k], col + dj[k]           # 놓은 지점에서 델타 탐색
            flip_list = []                              # 자기가 먹을 돌 리스트 초기화
            # 인덱스 범위를 벗어나지않고, 자기와 다른 색 돌을 만날 때 까지
            while 0 <= ni < N and 0 <= nj < N and table[ni][nj] != 0 and table[ni][nj] != color:
                flip_list.append((ni, nj))      # 먹을 돌 리스트에 추가
                ni += di[k]                     # 델타 방향으로 한 칸 더
                nj += dj[k]
            # 추가된 먹을 돌 리스트에서 인덱스 값 뽑아서 뒤집기
            if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == color: # 델타 방향으로 한 칸 더 간 ni, nj가 본인 컬러 -> 그 사이에 있던 flip_list는 다른 색 돌이라는 말
                for flip_i, flip_j in flip_list:
                    table[flip_i][flip_j] = color

    w_count = 0
    b_count = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                b_count += 1
            elif table[i][j] == 2:
                w_count += 1

    print(f'#{test_case} {b_count} {w_count}')
