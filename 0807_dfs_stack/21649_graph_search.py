def DFS(start, V):
    invited = [0] * (V+1)
    invited[start] = 1
    answer = []
    stack = []
    answer.append(start)
    v = start
    while True:
        for w in adjV[v]:
            if invited[w] == 0:
                stack.append(v)
                v = w
                answer.append(v)
                invited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

    reanswer = '-'.join(map(str,answer))
    return reanswer




T = 1
for test_case in range(1,T+1):
    V, E = map(int, input().split())
    adjV = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjV[v1].append(v2)
        adjV[v2].append(v1)
    a = DFS(1,V)
    print(f'#{test_case} {a}')