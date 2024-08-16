T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for j in range(N):
        i = 0
        while i < N-1:
            if arr[i][j] == 1:
                for x in range(i+1, N):
                    if arr[x][j] == 2:
                        count += 1
                        i = x+1
                        break #for x
                    elif x == N-1 and arr[x][j] != 2:
                        i = N-1
                        break # for x
            else:
                i += 1

    print(count)

