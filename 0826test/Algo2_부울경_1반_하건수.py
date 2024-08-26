def dfs(n, sm, k):
    # 시작 위치, 위험도 합계, 더한 줄 초기값
    global ans
    # 3줄이 더해졌다면, ans와 비교하여 최솟값 입력
    if k == 3:
        ans = min(ans, sm)
        return
    # 시작 줄은 이미 방문한 것으로 표시
    visited[n] = 1

    # 방문하지 않은 줄이며, 이전 줄과 같은 줄이 아닐 경우에 방문
    for j in range(N):
        if n != j and visited[j] == 0:
            visited[j] = 1
            dfs(j, sm+danger[n][j], k+1)
            # 다음 경우의 수로 넘어갈 땐 방문한 줄은 다시 초기화
            visited[j] = 0

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    danger = [list(map(int, input().split())) for _ in range(N)]

    # 정답 출력할 최소 위험도 초기 설정
    ans = float('inf')

    # 이미 줄을 섰던 열이라면 visited 체크
    # 시작 위치와 위험도 합계 초기값
    for i in range(N):
        visited = [0] * N
        dfs(i, 0, 1)

    print(f'#{test_case} {ans}')