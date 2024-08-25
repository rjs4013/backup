from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))

    n_list = deque()

    for i in range(N):
        n_list.append(numbers[i])


    cnt = 0
    while cnt < M:
        a = n_list.popleft()
        n_list.append(a)
        cnt += 1

    ans = n_list[0]

    print(f'#{test_case} {ans}')




