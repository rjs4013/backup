def parenthesis(text):
    stack = []
    parenthesis_dic = {")": "(", "}": "{", "]": "["}
    for char in text:
        if char in parenthesis_dic.values():
            stack.append(char)
            continue

        if char in parenthesis_dic.keys():
            if not stack:
                return False
            if stack[-1] != parenthesis_dic[char]:
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
        print(f'#{test_case} 0')




# T = int(input())
# for test_case in range(1, T+1):
#     text = input()
#     stack = []
#     parenthesis_dic = {")":"(", "}":"{","]":"["}
#     answer = 0
#
#     for char in text:
#         if char in parenthesis_dic.values():
#             stack.append(char)
#             continue
#
#         if char in parenthesis_dic.keys():
#             if not stack:
#                 answer = 0
#             if stack[-1] != parenthesis_dic[char]:
#                 answer = 0
#             stack.pop()
#
#     if len(stack) == 0:
#         answer = 1
#     else:
#         answer = 0
#
#     print(f'#{test_case} {answer}')