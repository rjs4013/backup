def lvr(A):
    global ans
    if A:
        lvr(tree[A][0])
        ans.append(A)
        lvr(tree[A][1])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    tree = [[0,0] for _ in range(N+1)]

    for i in range(1, N//2+1):
        tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1

    ans = [] # [4,2,5,1,6,3]
    lvr(1)

    re_ans = []
    root = []
    for k, v in enumerate(ans):
        if v == N//2:
            re_ans.append(k+1)
        if v == 1: # root
            root.append(k+1)

    a = ''.join(map(str, root))
    b = ''.join(map(str, re_ans))

    print(f'#{test_case} {a} {b}')







