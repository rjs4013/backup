T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    M = N//2
    count = 0
    for i in range(N):
        if i <= M:
            for j in range(M-i,M+i+1):
                count += arr[i][j]
        else:
            for y in range(i-M, N-(i-M)):
                count += arr[i][y]
    print(f'#{test_case} {count}')

'''
델타로 접근하면 ㅈㅈ
중간 일자 줄 찾고 위 아래 M보다 크고 작은 행으로조건 나눠서 열 나뉘어지는 규칙찾기
'''