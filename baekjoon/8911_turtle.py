'''
F, B는 이동(앞, 뒤)
L, R은 방향 전환(왼, 오)
거북이가 지나간 x좌표 선, y좌표 선이 각 직사각형의 한 변이 됨.
'''
T = int(input())
for _ in range(T):
    arr = input()
    x, y, direction = 0, 0, 0 # 초기 거북이 위치, 방향값 설정
    # 거북이 지나간 경로 최대, 최소값 저장
    max_x, min_x = 0, 0
    max_y, min_y = 0, 0
    # 이동 시작
    for com in arr:
        if com == 'F': # 전진
            if direction == 0: # 북
                y += 1
            elif direction == 1: # 동
                x += 1
            elif direction == 2: # 남
                y -= 1
            else: # 서
                x -= 1

        elif com == 'B': # 후진
            if direction == 0: # 북
                y -= 1
            elif direction == 1: # 동
                x -= 1
            elif direction == 2: # 남
                y += 1
            else: # 서
                x += 1

        elif com == 'L':  # 좌회전
            if direction == 0:
                direction = 3  # 북쪽에서 좌회전 -> 서쪽
            else:
                direction -= 1

        elif com == 'R':  # 우회전
            if direction == 3:
                direction = 0  # 서쪽에서 우회전 -> 북쪽
            else:
                direction += 1

        # 이동 완료되면 좌표 갱신
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    w = max_x - min_x # 최종 가로 길이
    h = max_y - min_y # 최종 세로 길이

    print(w*h)