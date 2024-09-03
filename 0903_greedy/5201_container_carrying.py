'''
-N개의 컨테이너, M대의 트럭, A도시에서 B도시로 운반
-트럭 당 한 개의 컨테이너 운반, 트럭 적재용량 초과 -> 운반 X
-최대 M대의 트럭이 편도로 한번만 운행
-이동한 화물의 총 중량이 최대가 되도록 컨테이너 옮김
-옮겨진 화물의 전체 무게 출력 ㄱㄱ
-BUT, 화물을 싣지 못한 트럭 있을수도? + 남는 화물이 있을 수도? + 컨테이너 못 옮기는 경우 0 출력
'''

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 그리디로 풀기기
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    total = 0
    for i in truck:
        for j in weight:
            if i >= j:
                total += j
                weight.remove(j)
                break
    print(f'#{test_case} {total}')


    # # 트럭의 적재용량과 컨테이너의 무게를 비교, 가장 작은 무게차이를 가진 컨테이너를 트럭에 실으면 최대값이 된다.
    # real_gotruck = [0]
    # for i in truck:
    #     mpos = 100
    #     gotruck = 0
    #     for j in weight:
    #         if i < j: continue
    #         pos = i - j
    #         if mpos > pos:
    #             mpos = pos
    #             gotruck = j
    #     if gotruck != 0:
    #         real_gotruck.append(gotruck)
    #         weight.pop(weight.index(gotruck))
    # print(f'#{test_case} {sum(real_gotruck)}')




