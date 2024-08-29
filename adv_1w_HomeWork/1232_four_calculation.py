def cal(left, right, oper):
    if oper == '+':
        return left + right
    elif oper == '-':
        return left - right
    elif oper == '*':
        return left * right
    elif oper == '/':
        return left // right
    # return eval(f'{left} {oper} {right}')

def lvr(a):
    if type(tree[a][2]) == int:
        return tree[a][2]

    left = lvr(tree[a][0])
    right = lvr(tree[a][1])
    return cal(left, right, tree[a][2])

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    tree = [list([0,0,0]) for _ in range(N+1)]

    for i in range(N):
        idx = int(arr[i][0])
        if len(arr[i]) == 4:
            tree[idx][0] = int(arr[i][2])
            tree[idx][1] = int(arr[i][3])
            tree[idx][2] = arr[i][1]
        else:
            tree[idx][2] = int(arr[i][1])

    ans = int(lvr(1))
    print(f'#{test_case} {ans}')
