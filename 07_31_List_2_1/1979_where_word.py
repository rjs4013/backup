# 흰 부분(1)이 3개 연달아 오면 가능 (가로 or 세로)

T = int(input())

for x in range(T):
    N, K = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]

    for y in range(N):
        arr[y].insert(0, 0)
        arr[y].append(0)
    arr.insert(0, [0]*(N+2))
    arr.append([0]*(N+2))

    count = 0
    for i in range(N+2):
        for j in range(N-K+3):
            if arr[i][j:j+K+2] == [0] + [1]*K + [0]:
                count += 1

    for i in range(N+2):
        for j in range(N+2):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(N+2):
        for j in range(N-K+3):
            if arr[i][j:j+K+2] == [0] + [1]*K + [0]:
                count += 1

    print(f'#{x+1} {count}')


