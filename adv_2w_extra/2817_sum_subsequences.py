'''
부분 집합 구해서 합이 k인 경우 cnt +1
'''
def sub(n, sum):
    global cnt
    if sum > K:
        return
    if sum == K:
        cnt += 1
        return
    if n == N:
        return

    sub(n+1, sum + arr[n])
    sub(n+1, sum)



T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    sub(0, 0)
    print(f'#{test_case} {cnt}')
