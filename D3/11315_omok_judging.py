T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    dxy =[[-1, 1],[0,1],[1,1],[1,0]] # 오른대각위, 오른, 오른대각아래, 아래 4방향 델타
    answer = ''
    for i in range(N):
        for j in range(N):
            for dx, dy in dxy:
                count = 0
                if arr[i][j] == 'o': count += 1
                for z in range(1,5):
                    nx = i + dx * z
                    ny = j + dy * z
                    if 0<=nx<N and 0<=ny<N:
                        if arr[nx][ny] == 'o': count += 1
                        else : break
                    else : break
                if count >= 5:
                    answer = 'YES'
                    break
    if answer == '': print(f'#{test_case} NO')
    else: print(f'#{test_case} {answer}')