'''
i번째 칸에 쓰여 있는 수 -> Ai
Ai 이하 만큼 오른쪽으로 떨어진 칸으로 한 번에 쩜프
ex) 3번째 칸에 쓰여진 수 -> 3이면? -> 4, 5, 6번째 칸 중 하나로 쩜프
내가 가려고 하는 곳이 0이면 안된다.. 0일때는?
DP?
'''
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

if N == 1: # 1칸만 있으면 점프 필요 x
    print(0)
else:
    # bfs
    jump = [0]*(N+1) # 해당 칸으로 오기까지 점프 수 저장
    queue = deque([1]) # 첫 칸에서 시작

    while queue:
        i = queue.popleft()
        if i + arr[i-1] >= N: # 현 위치에서 적힌 칸 수를 점프할 때 N 또는 N을 초과한다면 종료
            print(jump[i]+1) # count 한번 더해주고
            break
        for j in range(1, arr[i-1]+1): # 현 위치에 적힌 칸 수 이하로 갈 수 있는 칸 순회
            ni = i + j
            if jump[ni] == 0: # 갔던 곳이 아니라면?
                queue.append(ni)
                jump[ni] = jump[i]+1 # 점프하기 전 칸의 점프수에 count + 1
    else:
        # while문이 break 되지 않았을 때는 실패로 간주
        print(-1)

















# cnt = 0
# current = 0
# while current < N:
#     if current + arr[current] >= N:
#         cnt += 1
#         break
#     if arr[current + arr[current]] != 0:
#         current += arr[current]
#         cnt += 1
#     else:
#         past = current
#         current += arr[current]
#         while arr[current + arr[current]] == 0:
#             current -= 1
#         if current == past:
#             cnt = -1
#             break
#         current += arr[current + arr[current]]
#         cnt += 1
#
# print(cnt)