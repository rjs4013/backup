T = int(input())
N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dxy = [[0, 1], [1, 0], [0, -1],[-1, 0]]


for test_case in range(1, T+1):
    answer = 0
    for i in range(N):
        for j in range(M):
            count = arr[i][j]
            for dx, dy in dxy:
                for a in range(1, arr[i][j]+1):
                    ni = i + dx * a
                    nj = j + dy * a
                    if 0<=ni<N and 0<=nj<M:
                        count += arr[ni][nj]
            if answer < count: answer = count
    print(f'#{test_case} {answer}')
