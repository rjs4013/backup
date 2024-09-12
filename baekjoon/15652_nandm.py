def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(1, N+1):
        if ans:
            if ans[-1] <= i:
                ans.append(i)
                dfs()
                ans.pop()
        else:
            ans.append(i)
            dfs()
            ans.pop()

N, M = map(int, input().split())
ans = []
dfs()