def fly(N, M, arr):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ai = [-1, 1, 1, -1]
    aj = [1, 1, -1, -1]
    for q in range(2, M):
        for w in range(4):
            di.append(di[w] * q)
            dj.append(dj[w] * q)
            ai.append(ai[w] * q)
            aj.append(aj[w] * q)

    answer1 = 0
    for i in range(N):
        for j in range(N):
            count = arr[i][j]
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    count += arr[ni][nj]
            if answer1 <= count:
                answer1 = count

    answer2 = 0
    for x in range(N):
        for y in range(N):
            count2 = arr[x][y]
            for k in range(len(di)):
                ni = x + ai[k]
                nj = y + aj[k]
                if 0<=ni<N and 0<=nj<N:
                    count2 += arr[ni][nj]
            if answer2 <= count2:
                answer2 = count2

    return max(answer1, answer2)


T = int(input())
for test_case in range(1, T+1):
    N, M =map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {fly(N, M, arr)}')