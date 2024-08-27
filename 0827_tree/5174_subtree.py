def preorder(A):
    global cnt
    if A:
        cnt +=1
        preorder(tree[A][0])
        preorder(tree[A][1])

T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))

    tree = [[0,0] for _ in range(E+2)]

    for i in range(len(nodes)//2):
        parent = nodes[i*2]
        child = nodes[i*2+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    cnt = 0
    preorder(N)


    print(f'#{test_case} {cnt}')