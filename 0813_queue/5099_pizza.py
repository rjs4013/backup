from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    # N = 화덕 크기, M = 피자 개수, cheese = 치즈 양
    N, M = map(int, input().split())
    pizza_cheese = list(map(int, input().split()))

    # 첫 화덕에 피자 정보를 큐로 저장 (피자 번호, 치즈 양) 튜플로
    oven = deque()
    for i in range(N):
        oven.append((i + 1, pizza_cheese[i]))

    # 화덕 넣은 피자 외 넣을 피자 인덱스
    pizza_next = N

    while len(oven) > 1:
        pizza_num, current_cheese = oven.popleft() # 화덕입구로 피자오면 빼서 피자 확인
        current_cheese //= 2  # 치즈의 양을 절반으로 줄이기

        # 치즈 다 녹았으면 다음 피자 넣기
        if current_cheese == 0:
            if pizza_next < M:
                oven.append((pizza_next + 1, pizza_cheese[pizza_next]))
                pizza_next += 1
        # 다 안녹았으면 치즈 녹인 피자 다시 넣기
        else:
            oven.append((pizza_num, current_cheese))

    print(f"#{test_case} {oven[0][0]}")
