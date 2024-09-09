n = int(input())
list_n = [int(input()) for _ in range(n)]
stack = []
list_ans = [] # 답 담을 리스트
cnt = 1       # 현재 넣어야 할 수

ans = True    # 수열 가능 여부

for k in list_n:
    while cnt <= k:     # 목표 하는 수인 K 가 나올 때 까지 PUSH
        stack.append(cnt)
        list_ans.append('+')
        cnt += 1

    if stack[-1] == k:  # 스택의 top이 k랑 같으면 pop 아니라면 수열 불가
        stack.pop()
        list_ans.append('-')
    else:
        ans = False
        break

if ans:
    print('\n'.join(list_ans))
else:
    print('NO')



