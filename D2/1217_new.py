T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 직선
    dxy2 = [[-1, 1], [1, 1], [1, -1], [-1, -1]] # 대각선
    maxcnt = 0
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            for dx, dy in dxy:
                for k in range(1, M):
                    ni = i+dx*k
                    nj = j+dy*k
                    if 0<=ni<N and 0<=nj<N:
                        cnt += arr[ni][nj]
            if maxcnt < cnt: maxcnt = cnt

            cnt = arr[i][j]
            for dx, dy in dxy2:
                for k in range(1, M):
                    ni = i + dx * k
                    nj = j + dy * k
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if maxcnt < cnt: maxcnt = cnt

    print(f'#{test_case} {maxcnt}')