T = int(input())
for x in range(T):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    real_sum = 0
    for i in range(N):
        for j in range(M):
            A = arr[i][j]
            di = []

            di.extend([0] * A)
            for y in range(1, A + 1):
                di.append(y)
            di.extend([0] * A)
            for r in range(1, A + 1):
                di.append(-r)

            dj = []
            for y in range(1, A + 1):
                dj.append(y)
            dj.extend([0] * A)
            for r in range(1, A + 1):
                dj.append(-r)
            dj.extend([0] * A)
            s = 0 + arr[i][j]
            for k in range(4*A):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    s += arr[ni][nj]
            if real_sum < s:
                real_sum = s
    print(real_sum)





