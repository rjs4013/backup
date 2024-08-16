import sys
sys.stdin = open("new.txt","r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    s = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                s +=arr[i][j]
            elif N-1-i == j:
                s +=arr[i][j]
    print(f'#{test_case} {s}')