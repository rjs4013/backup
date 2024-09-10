T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    three = [[] for _ in range(9)]
    a = 0

    for k in range(0 ,8, 3):
        b = 0
        for _ in range(3):
            for i in range(k, k+3):
                for j in range(0+b, 3+b):
                    three[a].append(arr[i][j])
            a += 1
            b += 3

    ans = 0
    for q in range(9):
        if len(set(arr[q])) != 9:
            ans = -1
            break
    else:
        arr1 = list(zip(*arr))
        for w in range(9):
            if len(set(arr1[w])) != 9:
                ans = -1
                break
        else:
            for e in range(9):
                if len(set(three[e])) != 9:
                    ans = -1
                    break

    if ans == 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')




