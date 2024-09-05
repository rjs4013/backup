'''
N명의 직원, N개의 할 일
1~N까지 번호 매김(직원, 할 일 둘 다)
I번 직원이 J번 일을 하면 성공할 확률 Pi,j
출력 : 주어진 일이 모두 성공할 확률의 최댓값
'''
def success(n, per):
    global ans
    if ans >= per:
        return

    if n == N:
        ans = max(ans, per)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            success(n+1, per * arr[n][i]/100)
            visited[i] = 0




T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [0] * N

    ans = 0

    success(0, 1)

    reans = "{:.6f}".format(ans*100)
    print(f'#{test_case} {reans}')