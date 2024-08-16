
T = int(input())
for test_case in range(1, T + 1):
    Forth = input().split()
    stack = []
    answer = []

    for i in Forth:
        if i.isdigit():
            stack.append(i)
        elif i == '+' or i == '-' or i == '*' or i == '/':
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == '+':
                    c = b + a
                    stack.append(c)
                elif i == '-':
                    c = b - a
                    stack.append(c)
                elif i == '*':
                    c = b * a
                    stack.append(c)
                elif i == '/':
                    if a == 0 or b == 0:
                        print(f'#{test_case} error')
                        break
                    else:
                        c = b / a
                        stack.append(c)
            else:
                print(f'#{test_case} error')
                break
        elif i == '.':
            if len(stack) == 1:
                print(f'#{test_case} {stack[0]}')
                break
            else:
                print(f'#{test_case} error')
                break
        else:
            print(f'#{test_case} error')
            break




