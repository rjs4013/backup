T = int(input())
for test_case in range(1, T+1):
    N, K = map(int,input().split())
    line = list(map(int, input().split()))

    # 미생물의 현재 위치 초기화
    bug = 1

    # 시작점부터
    i = 0
    while i < N-1:
        # 먹이감 line 에서 현 위치가 1이면 그 위치로 이동할 것
        if line[i] == 1:
            # 만약 내 위치에서 미생물을 먹고 K로 위치로 가는 경로에 1이 있는 경우엔 1이 위치한 인덱스만큼 +
            if 1 in line[i+1:i+K-1]:
                bug += line[i+1:i+K-1].index(1)+1
                i += line[i+1:i+K-1].index(1)+1
                # 미생물이 line 범위를 벗어나버리면 최대 이동값은 N
                if bug > N:
                    bug = N
            else:
                bug += K
                i += K
                # 미생물이 line 범위를 벗어나버리면 최대 이동값은 N
                if bug > N:
                    bug = N
        # 현 위치가 0이면 while문 종료
        else: break

    print(f'#{test_case} {bug}')