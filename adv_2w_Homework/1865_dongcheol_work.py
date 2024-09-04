'''
N명의 직원, N개의 할 일
1~N까지 번호 매김(직원, 할 일 둘 다)
I번 직원이 J번 일을 하면 성공할 확률 Pi,j
출력 : 주어진 일이 모두 성공할 확률의 최댓값
'''

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

