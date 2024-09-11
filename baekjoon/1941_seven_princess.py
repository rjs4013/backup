'''
이다솜파(S)...임도연파(Y)...
1. 7명의 여학생들로 구성되어야 한다.
2. 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
3. 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
4. ‘이다솜파’가 반드시 우위를 점해야 한다.
   따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
'''
from collections import deque

# 칠공주가 인접하는지 확인할 bfs
def bfs(si, sj):
    q = deque()
    # 새로운 v 배열 생성
    visited_2 = [[0]*5 for _ in range(5)]

    q.append((si, sj))
    visited_2[si][sj] = 1
    cnt = 1
    # 네 방향 확인하면서 인접한지 체크
    dxy = [[0,1], [1, 0], [0, -1], [-1, 0]]
    while q:
        ci, cj = q.popleft()
        for dx, dy in dxy:
            ni = ci + dx
            nj = cj + dy
            # 4방향, 범위 내, 미방문, 칠공주인지 체크
            if 0<=ni<5 and 0<=nj<5 and visited_2[ni][nj] == 0 and visited[ni][nj] == 1:
                q.append((ni, nj))
                visited_2[ni][nj] = 1
                cnt += 1
    return cnt == 7 # cnt가 7이면 true

# 칠공주인지 체크할 시작 칸 찾기
def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j]==1:
                return bfs(i,j)

def dfs(n, cnt, s_cnt):
    global ans
    if cnt > 7:
        return

    # 끝 칸까지 오게 되면, 칠공주이며, 다솜파가 4명이상이다 -> 인접한 7명인지 체크 후 ans +1
    if n == 25:
        if cnt == 7 and s_cnt >= 4:
            if check():
                ans += 1
        return

    # 2차원 배열을 1차원으로 변환..
    visited[n//5][n%5] = 1 # 포함하는 경우
    dfs(n+1, cnt+1, s_cnt+int(arr[n//5][n%5]=='S')) # int 괄호 내 저게 맞으면 +1, 아니면 +0
    visited[n//5][n%5] = 0 # 원상 복구
    dfs(n+1, cnt, s_cnt)   # 포함하지 않는 경우


arr = [input() for _ in range(5)]
ans = 0
visited = [[0] * 5 for _ in range(5)]
# 학생번호(0~24), 포함학생 수, 다솜파 학생 수
dfs(0,0,0)
print(ans)







# def dfs(x, y, n, S):
#     # 종료 조건 : 7개 탐색 완료했고, 이다솜파가 4명 이상이다.
#     if n == 7 and S >= 4:
#         return True
#     # 방문 체크
#     visited[x][y] = True
#
#     # 상하 좌우 탐색
#     dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     # 결과 값 저장할 곳(True, False)
#     result = False
#
#     for dx, dy in dxy:
#         nx = x + dx
#         ny = y + dy
#         # 업뎃된 위치가 'S'면 깊이 증가, 'S' 개수도 1 증가 DFS 호출
#         if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and arr[nx][ny] == 'S':
#             if dfs(nx, ny, n+1, S+1):
#                 result = True
#         # 업뎃된 위치가 'Y'면 깊이만 증가 DFS 호출
#         elif 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and arr[nx][ny] == 'Y':
#             if dfs(nx, ny, n+1, S):
#                 result = True
#
#     # visited 복구 시키기
#     visited[x][y] = False
#     return result
#
#
# arr = [list(map(str,input())) for _ in range(5)]
# cnt = 0
#
# for i in range(5):
#     for j in range(5):
#         # 'S'로 시작할 때만 탐색함
#         if arr[i][j] == 'S':
#             # 시작점마다 방문 상태 초기화
#             visited = [[False] * 5 for _ in range(5)]
#             if dfs(i, j, 1, 1): # 현재 점 포함한거니, 깊이도 1로 시작, 'S'로 시작하니 S 개수도 1
#                 cnt += 1 # True로 반환되면 cnt +1
# print(cnt)