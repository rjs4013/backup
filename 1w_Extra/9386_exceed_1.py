T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(input())
    maxcnt = 0
    cnt = 0
    for a in range(len(numbers)):
        if numbers[a] == '0':
            cnt = 0
        if numbers[a] == '1':
            cnt += 1
        if maxcnt < cnt: maxcnt = cnt

    print(f'#{test_case} {maxcnt}')
