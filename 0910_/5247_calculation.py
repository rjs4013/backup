'''
- 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
- 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소
    몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
'''
from collections import deque
def bfs(N, cal):
    queue = deque()
    queue.append()


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())s
    ans = 10000
    bfs(N, 0)
    print(f'#{test_case} {ans}')