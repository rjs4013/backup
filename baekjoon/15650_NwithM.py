'''
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
'''
def run(lev, start):
    # M개 골라지면 ans에 있는거 print 찍고 빠져나가기
    if lev == M:
        print(*ans)
        return
    for k in range(start, N):
        ans.append(num[k])
        run(lev + 1, k + 1)
        # print 찍힌 후엔 pop
        ans.pop()


N, M = map(int, input().split())

num = []
for i in range(1, N+1):
    num.append(i)
ans = []
run(0,0)
