T = 10
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(input())
    stack = []
    answer = 0
    for i in numbers:
        if i.isdigit():
            stack.append(i)
            if len(stack) == 2:
                answer = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(answer)
    print(f'#{test_case} {answer}')