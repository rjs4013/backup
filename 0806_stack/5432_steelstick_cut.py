'''
'(' 나오면 스택 넣기 -> 레이저이거나..쇠막대기의 시작이거나..
')' 나오면 스택.pop -> pop된 '(' 이 레이저인지 막대긴지 판단
    => 직전 문자가 '(' 이라면 레이저 -> 현재 스택에 남은 개수 만큼 쇠막대기 잘림
    => else? -> 쇠막대기의 끝임, 쇠막대기 하나가 끝났으니까 스택 남은 '(' 만큼 쇠막대기 조각 증가
'''
T = int(input())
for test_case in range(1, T+1):
    arr = list(map(str,input()))

    stack = []
    cnt = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if arr[i-1] == '(':
                cnt += len(stack)
            else:
                cnt += 1

    print(f'#{test_case} {cnt}')





