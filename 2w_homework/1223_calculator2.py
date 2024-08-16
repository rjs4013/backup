T = 10
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(input())
    stack = []
    stack_cal = [0]
    cal_dic = {'+' : 1, '*' : 2}
    for i in numbers:
        if i.isdigit():
            stack.append(i)
        elif i == '+':
            stack_cal.append(i)
            if stack_cal[-2] == '+' and len(stack) >= 2:
                a = int(stack[-1]) + int(stack[-2])
                stack.append(a)
                stack.pop(-2)
                stack.pop(-2)

                stack_cal.pop()
            elif stack_cal[-2] == '*' and len(stack) >= 2:
                a = int(stack[-1]) * int(stack[-2])
                stack.append(a)
                stack.pop(-2)
                stack.pop(-2)

                stack_cal.pop(-2)
        elif i == '*':
            stack_cal.append(i)
            if stack_cal[-2] == '+' and len(stack) > 2:
                a = int(stack[-1]) * int(stack[-2])
                stack.append(a)
                stack.pop(-2)
                stack.pop(-2)

                stack_cal.pop()
            if stack_cal[-2] == '+' and len(stack) > 2:
                a = int(stack[-1]) * int(stack[-2])
                stack.append(a)
                stack.pop(-2)
                stack.pop(-2)

                stack_cal.pop()
    ans = 0
    for j in range(len(stack)-1):
        ans += int(stack[j]) + int(stack[j+1])

    print(ans)



