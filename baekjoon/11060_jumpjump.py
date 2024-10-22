'''
i번째 칸에 쓰여 있는 수 -> Ai
Ai 이하 만큼 오른쪽으로 떨어진 칸으로 한 번에 쩜프
ex) 3번째 칸에 쓰여진 수 -> 3이면? -> 4, 5, 6번째 칸 중 하나로 쩜프
내가 가려고 하는 곳이 0이면 안된다.. 0일때는?
'''

N = int(input())
arr = list(map(int, input().split()))

cnt = 0
current = 0
while current < N:
    if current + arr[current] >= N:
        cnt += 1
        break
    if arr[current + arr[current]] != 0:
        current += arr[current]
        cnt += 1
    else:
        current += arr[current]
        past = current - 1
        while arr[current + arr[current]] == 0:
            current -= 1
        if current < past:
            cnt = -1
            break
        current += arr[current + arr[current]]
        cnt += 1

print(cnt)