def lvr(a):
    global ans
    if a:
        lvr(tree[a][0])
        ans.append(a)
        lvr(tree[a][1])

T = int(input())
for test_case in range(1,T+1):
    N = int(input())

    tree = [[0,0] for _ in range(N+1)]
    for i in range(1,N//2+1):
        tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1

    ans = []
    lvr(1)

    ans1 = 0
    ans2 = 0

    for k, v in enumerate(ans):
        if v == N // 2:
            ans1 = k + 1
        if v == 1:
            ans2 = k + 1
    print(f'#{test_case} {ans2} {ans1}')