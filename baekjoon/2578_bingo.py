arr = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]


cnt = 0
ans = 0
while cnt < 3:
    for i in range(5):
        for j in range(5):
            cnt = 0
            # 가로
            for a in range(5):
                for b in range(5):
                    if arr[a][b] != call[i][j]: continue
                    arr[a][b] = 0
                if sum(arr[a][:5]) == 0: cnt += 1

            # 대각선
            z = 0
            s = 0
            for k in range(5):
                if arr[k][4-k] == 0: z += 1
                if arr[k][k] == 0 : s += 1
            if z == 5: cnt += 1
            if s == 5: cnt += 1
            # 세로
            for q in range(5):
                c = 0
                for w in range(5):
                    if arr[w][q] == 0:
                        c += 1
                if c != 5: continue
                cnt += 1

            if cnt >= 3:
                ans = i*5+j+1
                break
        if cnt >= 3: break
print(ans)
