'''
동근이 위치 -> X
블록의 크기, 상점의 개수 및 위치, 동근이의 위치
출력 -> 동근이의 위치에서 각 상점 사이의 최단 거리 합
(상점이 위치한 방향)1, 2, 3, 4 -> 북, 남, 서, 동
(상점 북 or 남 ) -> 블록의 '왼쪽' 경계로부터의 거리
(상점 동 or 서 ) -> 블록의 '위쪽' 경계로부터의 거리
'''

x, y = map(int, input().split())
stores = int(input())  # 상점 수
info = []  # 상점 위치 정보

for _ in range(stores):
    direction, distance = map(int, input().split())
    info.append((direction, distance))

info_dong = list(map(int, input().split()))  # 동근이 정보

total_distance = 0

for direction, distance in info:
    if direction == info_dong[0]:  # 동근 - 상점 같은 방향
        dis = abs(distance - info_dong[1])
    else:
        if info_dong[0] == 1:  # 동근이 북쪽
            if direction == 2:  # 상점 남쪽
                dis = min(y + info_dong[1] + distance, y + (x - distance) + (x - info_dong[1]))
            elif direction == 3:  # 상점 서쪽
                dis = info_dong[1] + distance
            elif direction == 4:  # 상점 동쪽
                dis = (x - info_dong[1]) + distance

        elif info_dong[0] == 2:  # 동근이 남쪽
            if direction == 1:  # 상점 북쪽
                dis = min(y + info_dong[1] + distance, y + (x - distance) + (x - info_dong[1]))
            elif direction == 3:  # 상점 서쪽
                dis = info_dong[1] + (y - distance)
            elif direction == 4:  # 상점 동쪽
                dis = (y - distance) + (x - info_dong[1])

        elif info_dong[0] == 3:  # 동근이 서쪽
            if direction == 1:  # 상점 북쪽
                dis = info_dong[1] + distance
            elif direction == 2:  # 상점 남쪽
                dis = (y - info_dong[1]) + distance
            elif direction == 4:  # 상점 동쪽
                dis = min(distance + (info_dong[1]) + x, (y - distance) + (y - info_dong[1]) + x)

        elif info_dong[0] == 4:  # 동근이 동쪽
            if direction == 1:  # 상점 북쪽
                dis = (x - distance) + info_dong[1]
            elif direction == 2:  # 상점 남쪽
                dis = (x - distance) + (y - info_dong[1])
            elif direction == 3:  # 상점 서쪽
                dis = min(distance + (info_dong[1]) + x, (y - distance) + (y - info_dong[1]) + x)

    total_distance += dis

print(total_distance)





