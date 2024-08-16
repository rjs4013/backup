# def BFS(G,v):  # 그래프 G, 탐색 시작점 v
#     visited = [0]*(n+1)                 # n: 정점의 개수
#     queue = []                          # 큐 생성
#     queue.append(v)                     # 시작점 v를 큐에 삽입
#     while queue:                        # 큐가 비어있지 않은 경우
#         t = queue.pop(0)                # 큐의 첫번째 원소 반환
#         if not visited[t]:              # 방문되지 않은 곳이라면
#             visited[t] = True           # 방문한 것으로 표시
#             visit(t)                    # 정점 t에서 할 일
#             for i in G[t]:              # t와 연결된 모든 정점에 대해
#                 if not visited[i]:      # 방문되지 않은 곳이라면
#                     queue.append(i)     # 큐에 넣기

# '''
# 7 8
# 4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
# '''
#
# def bfs(s, V):  # 시작정점 s, 마지막 정점 V
#     visited = [0] * (V+1)   # visited 생성
#     q = []          # 큐 생성
#     q.append(s)     # 시작점 인큐
#     visited[s] = 1  # 시작점 방문표시
#     while q:        # 큐에 정점이 남아있으면 front != rear
#         t = q.pop(0)    # 디큐
#         print(t)        # 방문한 정점에서 할일
#         for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
#             if visited[w]==0:
#                 q.append(w)     # w인큐, 인큐되었음을 표시
#                 visited[w] = visited[t] + 1
#
# V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
# arr = list(map(int, input().split()))
# # 인접리스트 -------------------------
# adj_l = [[] for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)    # 방향이 없는 경우
# # 여기까지 인접리스트 -----------------
# bfs(1, 7)




