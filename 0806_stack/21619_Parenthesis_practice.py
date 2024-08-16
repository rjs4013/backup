def parenthesis(text):
    stack = []
    n_dict = {')':'(', '}':'{', ']':'['}
    for i in text:
        if i in n_dict.values():
            stack.append(i)
            continue
        if i in n_dict.keys():
            if not stack or stack[-1] != n_dict[i]:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


T = int(input())
for test_case in range(1, T+1):
    text = input()
    if parenthesis(text) is True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} -1')

