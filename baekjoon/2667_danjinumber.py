'''
출력 -> 총 단지의 수, 각 단지에 속하는 집의 수 오름차순 출력
'''
from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(i, j):
    global cnt
    queue = deque([(i, j)])
    while queue:
        i, j = queue.popleft()
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                queue.append((ni,nj))
                visited[ni][nj] = 1
                cnt += 1



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = []    # 단지내 집 몇갠지 저장할 리스트
total = 0   # 단지 수 저장

for i in range(N):
    for j in range(N):
        cnt = 0
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            if cnt == 0: cnt += 1 # 단지에 집이 하나일 때도 카운트해줘
            ans.append(cnt)
            total += 1

reans = sorted(ans)

print(total)
for r in range(len(reans)):
    print(reans[r])