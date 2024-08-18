'''
첫 번째 수 - 양의 정수
두 번째 수 - 양의 정수 中 1개 선택
세 번째 이후 - 앞의 앞의 수에서 앞의수를 빼서 만들기(세번째 수 = 첫번째 수 - 두번째 수)
음의 정수가 만들어지면 버리고 종료
최대 개수의 수들 빈칸 두고 출력
'''
N = int(input())
reans = []
for i in range(1,N+1):
    ans = [N]
    ans.append(i)

    for j in range(N+1):
        if ans[j] - ans[j+1] < 0: break
        else: ans.append(ans[j] - ans[j+1])

    if len(reans) < len(ans): reans = ans

realans = ' '.join(map(str, reans))
print(len(reans))
print(realans)

