def lvr(A):
    global ans
    if A:
        lvr(tree[A][0])
        ans.append(tree[A][2])
        lvr(tree[A][1])


T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [0] + [list(map(str,input().split())) for _ in range(N)]
    tree = [[0,0] for _ in range(N+1)]


    for i in range(1, len(arr)):
        if len(arr[i]) == 4:
            tree[i][0] = arr[i][2]
            tree[i][1] = arr[i][3]
        elif len(arr[i]) == 3:
            tree[i][0] = arr[i][2]
    for j in range(1, len(arr)):
        tree[j].append(arr[j][1])

    tree[0] = ['0','0','0']

    tree = [[int(info[0]), int(info[1]), info[2]] for info in tree]

    ans = []

    lvr(1)
    result = ''.join(map(str, ans))
    print(f'#{test_case} {result}')



