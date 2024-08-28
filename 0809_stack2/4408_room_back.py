'''
학생들이 방 번호 구간에서 이동하는 걸 복도 번호로 변환
ex) 1번 방 -> 2번 방 : 1번 복도 사용

복도 번호가 겹친다면? +1 시간
'''

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []

    for _ in range(N):
        start, end = map(int,input().split())
        # 항상 방번호가 작은 쪽에서 큰 쪽으로 이동하도록 만듦 -> 안 그러면 밑에 for 문 돌릴때 에러남
        if start > end: start, end = end, start
        arr.append((start,end))

        room_road = [0] * 200 # 방이 400개면 복도는 200개

    for start, end in arr:
        # 해당 학생이 지나가는 복도에 +1
        for i in range((start-1)//2, (end-1)//2 + 1): # 복도 1개는 방2개임... 1번 방이 해당되는 복도는? 0번 복도
            room_road[i] += 1

    # 이동 경로가 겹친다? 이 복도를 통과하기 위해선 겹치는 학생 수만큼의 시간 필요 -> 최소 시간
    ans = max(room_road)

    print(f'#{test_case} {ans}')