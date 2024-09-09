'''
이다솜파(S)...임도연파(Y)...
1. 7명의 여학생들로 구성되어야 한다.
2. 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
3. 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
4. ‘이다솜파’가 반드시 우위를 점해야 한다.
   따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
'''
def dfs(x, y, n, S):
    if n == 7 and S >= 4:
        return True
    visited[x][y] = True

    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and arr[nx][ny] == 'S':
            dfs(nx, ny, n+1, S+1)
        elif 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and arr[nx][ny] == 'Y':
            dfs(nx, ny, n+1, S)



arr = [list(map(str,input())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        if dfs(i, j, 1, 0) == True:
            cnt += 1