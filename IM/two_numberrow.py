def twonumber(N, M, Ai, Bj):
    max_sum = 0
    if M > N:
        ran = M - N + 1
        for i in range(ran):
            i_sum = []
            for j in range(N):
                a = Ai[j] * Bj[j+i]
                i_sum.append(a)
            b = sum(i_sum)
            if max_sum < b:
                max_sum = b
    else:
        ran = N - M + 1
        for i in range(ran):
            i_sum = []
            for j in range(M):
                a = Ai[j+i] * Bj[j]
                i_sum.append(a)
            b = sum(i_sum)
            if max_sum < b:
                max_sum = b
    return max_sum



T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    print(f'#{test_case} {twonumber(N, M, Ai, Bj)}')
