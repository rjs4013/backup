T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    num = 1
    top, bottom = 0, N-1
    left,right = 0, N-1

    while top <= bottom and left <= right:
        for i in range(left, right +1):
            arr[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom +1):
            arr[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left -1, -1):
            arr[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top -1, -1):
            arr[i][left] = num
            num += 1
        left += 1

    print(f'#{test_case}')

    for a in arr:
        print(' '.join(map(str, a)))
    # print(real_arr)
