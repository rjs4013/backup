def secret_number(num, N):
    stack = []
    for i in range(N):
        if num[i] not in stack or num[i] != stack[-1]:  # 스택에 num[i]가 없거나 스택의 마지막과 num[i]가 같지 않을때
            stack.append(num[i])                        # 스택에 num[i] 추가
        elif num[i] == stack[-1]:                       # 직전에 들어간 문자랑 지금 들어간 문자랑 같을 때
            stack.pop()                                 # 스택에서 빼내기(중복된 문자 제거)
    answer = ''.join(stack)
    return answer


T = 2
for test_case in range(1, T+1):
    n, num = input().split()
    N = int(n)
    print(f'#{test_case} {secret_number(num, N)}')