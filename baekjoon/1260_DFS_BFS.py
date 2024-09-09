'''
N -> 정점의 개수
M -> 간선의 개수
V -> 탐색을 시작할 정점의 번호
'''
from collections import deque

def dfs(num):           # 시작 정점부터 탐색
    visited[num] = True # 방문 표시
    ans_dfs.append(num)

    for i in node[num]: # 해당 정점에서 갈 수 있는 정점들 탐색
        if not visited[i]: # 방문하지 않은 정점일 때 이동
            dfs(i)

def bfs(renum):
    queue = deque([renum])
    visited[renum] = True
    while queue:
        # 큐에서 원소 뽑아서 답 리스트에 추가
        q = queue.popleft()
        ans_bfs.append(q)
        # 아직 방문하지 않은 인접 정점들 큐에 삽입
        for j in node[q]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

N, M, V = map(int,input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    node[start].append(end)
    node[end].append(start)

# 정점 번호가 작은 것 먼저 방문 위함
for k in node:
    k.sort()

visited = [False] * (N+1)
ans_dfs = []
ans_bfs = []
dfs(V)
# 방문 초기화
visited = [False] * (N+1)
bfs(V)
print(*ans_dfs)
print(*ans_bfs)
