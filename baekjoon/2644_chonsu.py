'''
x는 y의 부모 번호
출력 -> 두 사람의 촌수 (두 사람의 친척 관계가 없을경우 -1 출력)
'''
def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)


n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] -1)