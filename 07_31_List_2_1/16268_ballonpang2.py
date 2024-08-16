import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    answer = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<M:
                    s += arr[ni][nj]
                if answer < s:
                    answer = s

    print(f'#{test_case} {answer}')