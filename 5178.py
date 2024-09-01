

T = int(input())
for test_case in range(1, T+1):
    N,M,L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num
    while N != L*2-1:
        child = N
        parent = N//2
        tree[parent] += tree[child]
        N -= 1
