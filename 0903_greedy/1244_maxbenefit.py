'''
정해진 횟수만큼 숫자판 교환, 받을 수 있는 가장 큰 금액 산출
'''
def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int(''.join(map(str, num))))
        return

    for i in range(L-1):
        v = []
        for j in range(i+1, L):
            num[i], num[j] = num[j], num[i]

            change = int(''.join(map(str, num)))
            if (n, change) not in v:
                dfs(n+1)
                v.append((n,change))
            num[i], num[j] = num[j], num[i]


T = int(input())
for test_case in range(1, T+1):
    a, N = map(int,input().split())
    num = list(map(int, str(a)))

    L = len(num)
    ans = 0
    dfs(0)
    print(f'#{test_case} {ans}')


    # for _ in range(N):
    #     change_front = 0
    #     change_back = 0
    #     for i in range(0, len(num)-1):
    #         if num[i] < max(num[i+1:]):
    #             change_front = i
    #             break
    #     for j in range(len(num)-1, 0, -1):
    #         if num[change_front] < num[j] and num[j] >= max(num[change_front:j]):
    #             change_back = j
    #             break
    #     num[change_front], num[change_back] = num[change_back], num[change_front]
    #
    # ans = ''.join(map(str, num))
    # print(f'#{test_case} {ans}')


