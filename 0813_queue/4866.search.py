T = int(input())
for test_case in range(1, T + 1):
    a = list(input())
    stack = []  # 스택으로 사용할 리스트

    ans = True  # 괄호가 올바른지 확인

    for char in a:
        if char == '{' or char == '(':
            stack.append(char)  # 열린 괄호는 스택에 추가
        elif char == '}' or char == ')':
            if not stack:
                ans = False
                break  # 닫는 괄호가 나왔는데 스택이 비어있으면 실패
            check = stack.pop()  # 스택의 맨 마지막 열린 괄호를 꺼냄
            if (check == '{' and char != '}') or (check == '(' and char != ')'):
                ans = False
                break  # 괄호의 짝이 맞지 않으면 실패

    # 스택에 열린 괄호가 남아있다면 실패
    if stack:
        ans = False

    result = 1 if ans else 0
    print(f"#{test_case} {result}")
