# T = int(input())
# for x in range(T):
#     N, K = list(map(int,input().split()))
#     arr = [1,2,3,4,5,6,7,8,9,10,11,12]
#     n = len(arr)
#     subset_cnt = 2**n
#
#     subsets = []
#     for i in range(subset_cnt):
#         subset = []
#         for j in range(n):
#             if i & (1 << j):
#                 subset.append(arr[j])
#         subsets.append(subset)
#     acount = 0
#     answer = 0
#     for o in range(len(subsets)):
#         if sum(subsets[o]) == K and len(subsets[o]) == N:
#             acount += 1
#     print(f'#{x+1} {acount}')

#백트래킹
def dfs(n, sm, cnt):
    global ans

    if sm > K or cnt > CNT: # 내려가다가 합이 K보다 커지면 리턴(백) OR 집합 내 원소 개수 초과 시 리턴(백)
        return

    if n == N:
        if sm == K and cnt == CNT:
            ans += 1
        return

    dfs(n + 1, sm + lst[n], cnt + 1)  # 사용
    dfs(n + 1, sm, cnt)               # 미사용


T = int(input())
for test_case in range(1, T + 1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 12

    ans = 0
    dfs(0, 0, 0)
    print(f'#{test_case} {ans}')
