'''
T에서 (와 )만 남기면 S가 만들어져야 한다.
T는 (,),1,+로만 이루어져야 한다. 특히, 수식의 중간에 공백 등 문자 X
'''

S = list(map(str,input()))

first_stack = []
second_stack = []

for i in S:
    if i == '(':
        first_stack.append(i)
    else:
        if first_stack:
            a = first_stack.pop()
            if second_stack:
                second_stack.append('+')
                second_stack.append(a * (1+len(first_stack)))
                second_stack.append(1)
                if len(first_stack) >= 1:
                    for j in range(len(first_stack)):
                        second_stack.append('+')
                        second_stack.append(1)
                second_stack.append(i)
                first_stack.clear()
            else:
                second_stack.append(a * (1+len(first_stack)))
                second_stack.append(1)
                if len(first_stack) >= 1:
                    for j in range(len(first_stack)):
                        second_stack.append('+')
                        second_stack.append(1)
                second_stack.append(i)
                first_stack.clear()
        else:
            second_stack.append('+')
            second_stack.append(1)
            second_stack.append(i)

ans = ''.join(map(str, second_stack))

print(ans)



