def repeatword(text):
    N = len(text)
    stack = []
    for i in range(N):
        if text[i] not in stack or text[i] != stack[-1]:    # 스택에 text의 i번째 글자가 없으면 or 직전 스택과 text의 i번째 글자가 일치하지 않을때 추가
            stack.append(text[i])
        elif text[i] == stack[-1]:                          # text의 i번째 글자가 직전 스택과 같다면
            stack.pop()                                     # 스택의 마지막 글자 빼내기
    return len(stack)                                       # 스택에 몇개있는지 세기



T = int(input())
for test_case in range(1, T+1):
    text = input()
    print(f'#{test_case} {repeatword(text)}')
