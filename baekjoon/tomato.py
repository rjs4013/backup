'''
하루가 지나면 익은 토마토의 인접한 곳의 안익은 토마토가 익어
인접 -> 위, 아래, 왼쪽, 오른쪽, 앞, 뒤(뒤 4개는 델타)
최소 며칠이 지나야 토마토가 다 익는지를 알고싶음
상자의 일부 칸에는 토마토가 없을수도있음
상자의 가로 -> M
상자의 세로 -> N
저장될 때 부터 모든 토마토가 익어있다? -> 0 출력
토마토 익지 못하는 상황이다? -> -1 출력
'''

from collections import deque
def bfs():
    # [1] q생성, v[]생성
    q = deque()
    v = [[[0]*M for _ in range(N)] for _ in range(H)]

    # [2] q에 초기데이터(들) 삽입, 안익은 토마토 카운트
    cnt = 0
    for h in range(H):              # 전체순회하며 처리
        for i in range(N):
            for j in range(M):
                if arr[h][i][j]==1: # 익은토마토
                    q.append((h,i,j))
                    v[h][i][j]=1
                elif arr[h][i][j]==0: # 안익은토마토
                    cnt += 1

    while q:
        ch,ci,cj = q.popleft()

        # 6방향, 범위내, 미방문, arr[] == 0
        for dh,di,dj in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)):
            nh,ni,nj = ch+dh, ci+di, cj+dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and v[nh][ni][nj]==0 and arr[nh][ni][nj]==0:
                q.append((nh,ni,nj))
                v[nh][ni][nj] = v[ch][ci][cj]+1 # 1일씩 추가
                cnt -= 1    # 안익은 토마토 1개 익음

    if cnt==0:              # 모든 토마토 익었음
        return v[ch][ci][cj]-1 # 첫 1일 빼주고
    else:
        return -1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)