'''
0시부터 다음날 0시 이전까지 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내리게
앞 작업의 종료와 동시에 다음 작업 시작 가능
'''

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    # 종료 시간을 기준으로 정렬
    time.sort(key=lambda x: x[1])

    cnt = 0
    last_end_time = 0

    for start, end in time:
        # 현재 작업의 시작 시간이 이전 작업의 종료 시간 이후라면 작업 선택
        if start >= last_end_time:
            cnt += 1
            last_end_time = end  # 선택한 작업의 종료 시간을 업데이트

    print(f'#{test_case} {cnt}')