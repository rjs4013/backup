T = int(input())
ans = []
for test_case in range(1, T+1):
    A, B, C, D = map(int, input().split())
    if B > C and D > A:
        a = min(B, D) - max(A, C)
    else:
        a = 0
    ans.append(a)
for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')