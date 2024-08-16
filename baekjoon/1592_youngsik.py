'''
원형으로 N 까지 적힌 자리에 앉는다.
1번 자리 공 -> 다른 사람에게 던짐 반복
한 사람이 공을 M번 받았으면 게임 끝(지금 받은 공 포함해서)
공을 M번 보다 적게 받은 사람이 공을 던질 떄,
현재 공 받은 횟수가 홀수다? 자기 현재 위치에서 시계방향 L번째 있는 사람에게 토스
현재 공 받은 횟수가 짝수다? 자기 현재 위치에서 반시계방향으로 L번째 있는 사람에게 토스
출력 : 공을 총 몇번 던지는가
'''

N,M,L = map(int, input().split())

friends = []
for i in range(1, N+1):
    friends.append(i)

cnt_ball = [0] * (N+1)
count = 0
cnt_ball[1] = 1
ball_spot = 1
while M not in cnt_ball:
    if cnt_ball[ball_spot] % 2 == 0:
        if ball_spot + L <= N:
            ball_spot += L
            count += 1
            cnt_ball[ball_spot] += 1
        else:
            ball_spot += L - N
            count += 1
            cnt_ball[ball_spot] += 1
    else:
        if ball_spot - L > 0:
            ball_spot -= L
            count += 1
            cnt_ball[ball_spot] += 1
        elif ball_spot - L <= 0:
            ball_spot = abs(ball_spot - L + N)
            count += 1
            cnt_ball[ball_spot] += 1
print(count)