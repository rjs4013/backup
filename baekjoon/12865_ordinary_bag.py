'''
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
물품의 수 : N
버틸 수 있는 무게 : K
각 물건의 무게 : W
물건의 가치 : V
'''
def dfs(n, weight, value):
    global ans
    if weight > K:
        return
    if weight == K:
        ans = max(ans, value)
        return
    if n == N:
        return
    dfs(n+1, weight + W[n][0], value + W[n][1])
    dfs(n+1, weight, value)

N, K = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, 0, 0)
print(ans)