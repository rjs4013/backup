def search_route(start):
    v = start
    end = 99
    invited = [0] * 101
    invited[start] = 1
    stack = []
    while True:
        if v == end:
            return 1

        for w in adjV[v]:
            if invited[w] == 0:
                stack.append(w)
                v = w
                break
        else:
            stack.pop()
            invited[v] = 1

            if not stack:
                return 0
            else:
                v = stack[-1]



T = 10
for _ in range(1, T + 1):
    test_case, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjV = [[] for _ in range(101)]
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjV[v1].append(v2)

    print(f'#{test_case} {search_route(0)}')