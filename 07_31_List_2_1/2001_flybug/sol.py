import sys
sys.stdin = open("real.txt","r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0]*(M-1)
    dj = []
    for o in range(1, M):
        dj.append(o)

    max_count =[]
    for Q in range(N):
        for j in range(N-M+1):
            count = 0
            for i in range(M):
                if Q+M <= N:
                    count += arr[Q+i][j]
                for x in range(M-1):
                    ni = Q + i + di[x]
                    nj = j + dj[x]
                    if 0<=ni<N and 0<=nj<N:
                        count += arr[ni][nj]
            max_count.append(count)

    answer_count = max(max_count)
    print(f'#{test_case} {answer_count}')


