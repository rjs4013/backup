T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    codelist = {
        '0, 0, 0, 1, 1, 0, 1': 0,
        '0, 0, 1, 1, 0, 0, 1': 1,
        '0, 0, 1, 0, 0, 1, 1': 2,
        '0, 1, 1, 1, 1, 0, 1': 3,
        '0, 1, 0, 0, 0, 1, 1': 4,
        '0, 1, 1, 0, 0, 0, 1': 5,
        '0, 1, 0, 1, 1, 1, 1': 6,
        '0, 1, 1, 1, 0, 1, 1': 7,
        '0, 1, 1, 0, 1, 1, 1': 8,
        '0, 0, 0, 1, 0, 1, 1': 9
    }

    start_i = 0
    start_j = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                start_i, start_j = i-1, j-1
                break
    ans = []
    cnt = 0
    while cnt <= 8:
        for k in codelist.keys():
            if k == map(str,arr[start_i:start_i+8][start_j]):
                ans.append(codelist.values(k))
                break
        cnt += 1
        start_i += 1
    print(ans)