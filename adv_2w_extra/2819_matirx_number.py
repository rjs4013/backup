'''
- 4*4 격자판, 0~9 까지 숫자 적혀있음
- 임의의 위치에서 시작, 여섯번 델타방향으로 이동, 각 칸에 적힌 숫자 이어붙임
- 거쳤던 격자칸 다시 가도 된다.
- 만들 수 있는 서로 다른 일곱 자리 수들의 개수 구하기
'''
def dfs(n,num,ci,cj):
    if n == CNT:
        sset.append(num)
        return
    dxy = [[0,1], [1,0], [0, -1], [-1, 0]]

    for dx, dy in dxy:
        ni = ci + dx
        nj = cj + dy
        if 0<=ni<N and 0<=nj<N:
            dfs(n+1, num*10 + arr[ni][nj], ni, nj)

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    sset = []
    N, CNT = 4, 7
    for si in range(N):
        for sj in range(N):
            dfs(1, arr[si][sj], si, sj)

    print(f'#{test_case} {len(set(sset))}')




