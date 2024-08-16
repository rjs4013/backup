# # memorization
# def fibo1(n):
#     # global memo
#     if n>= 2 and memo[n] == 0:
#         memo[n] = fibo1(n-1) + fibo1(n-2)
#     return memo[n]
#
# n = 7
# memo = [0] * (n+1)
# memo[0] = 0
# memo[1] = 1
# fibo1(n)
# print(memo) # [0, 1, 1, 2, 3, 5, 8, 13]
# ---------------------------------------------
# 피보나치 수 DP 적용 알고리즘
# def fibo2(n):
#     f = [0] * (n+1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n+1):
#         f[i] = f[i-1] + f[i-2]
#
#
#     return f[n]
# ---------------------------------------------
# DFS 알고리즘
# visited[], stack[] 초기화
# DFS(v)
#     시작점 v 방문;
#     visited[v] <- true; # 방문했다고 표시
#     while True:
#         if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
#             push(v);
#             v <- w; (w에 방문)
#             visited[w] <- true;
#         else:
#             if (스택이 비어 있지 않으면)
#                 v <- pop(stack);
#             else
#                 break # 시작점으로 온 것
# end DFS()
# ---------------------------------------------
# DFS 1
'''
input
7 8 (정점의 개수 / 간선의 개수)
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def DFS(start, V):                      # start = 시작정점, V = 정점 개수(1번부터인 정점의 마지막 정점)
    visited = [0] * (V+1)               # 방문한 정점을 표시
    stack = []                          # 스택 생성
    print(start)
    visited[start] = 1                  # 시작 정점 방문 표시
    v = start                           # 현재 정점에서 시작
    while True:
        for w in adjL[v]:               # v에 인접하고, 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)         # push(v) 현재 정점을 push하고
                v = w                   # w에 방문
                print(v)
                visited[w] = 1          # w에 방문 표시
                break  #for w에 대한     # v부터 다시 탐색
        else:                           # 남은 인접정점이 없어서 break가 걸리지 않은경우
            if stack:                   # 이전 갈림길을 스택에서 꺼내서...if TOP -> -1
                v = stack.pop()
            else:                       # 되돌아갈 곳이 없으면, 남은 갈림길이 없으면 탐색종료
                break  #while True에 대한


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # adj[0] -> X
    # adj[1] -> 1에 인접인 정점
    adjL = [[] for _ in range(V+1)]
    arr = list(map(int,input().split()))
    # 인풋 2번째 값을 2개씩 가져오는 작업
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    DFS(1, V)