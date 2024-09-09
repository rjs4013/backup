'''
출력 -> 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
'''
def dfs(num):
    global cnt
    visited[num] = True

    for i in arr[num]:
        if visited[i] == False:
            # 방문 가능한 곳(감염되는 곳)이면 cnt += 1
            cnt += 1
            dfs(i)


N = int(input())
C = int(input())
arr = [[] for _ in range(N+1)]

# 그래프 연결 저장하기
for i in range(C):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

visited = [False] * (N+1)
cnt = 0
# 1번 컴퓨터에서 시작
dfs(1)

print(cnt)
