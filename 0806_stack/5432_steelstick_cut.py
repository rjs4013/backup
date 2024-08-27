'''
결국 쇠 막대기 안에 몇개의 레이저가 있는가? 가 핵심
cnt = 레이저 개수 + 1
'''
T = int(input())
for test_case in range(1, T+1):
    arr = list(map(str,input()))

    stack = []
    lazer = 0
    # for i in range(a):
    #     if arr[i] == '(' and arr[i+1] == ')':
    #         lazer += 1
    #     elif arr[i] == '(':
    #         stack.append(arr[i])
    #     elif arr[i] == ')' and arr[i-1] != '(':
    #         stack.pop(-1)

    for k, v in enumerate(arr):
        if v == '(' and arr[k+1] == ')':
            lazer += 1
        elif v == '(':
            stack.append((k,v))
        elif v == ')' and arr[k-1] != '(':
            a = stack.pop(-1)




