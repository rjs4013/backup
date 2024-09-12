def dfs():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(1, N+1):
        ans.append(i)
        dfs()
        ans.pop()

N, M = map(int, input().split())
ans = []
dfs()