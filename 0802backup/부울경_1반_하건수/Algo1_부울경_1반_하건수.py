T = int(input())
for test_case in range(1, T+1):
    N = int(input())                                        # 입력받을 행의 개수
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열 입력
    di = [0, 1, 0, -1]                                      # 우하좌상 이동(행)
    dj = [1, 0, -1, 0]                                      # 우하좌상 이동(열)
    answer_list = []                                        # 최종 맥스값 도출할 빈리스트 형성
    for i in range(N):
        for j in range(N):
            count = arr[i][j]                               # 해당 칸에 있는 미생물 개수 count에 입력
            for k in range(4):                              # 4방향 움직이는 반복문
                ni = i + di[k]                              # 방향별 이동 좌표설정
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    count += arr[ni][nj]                    # count에 이동된 좌표에 있는 미생물 개수 더하기
            answer_list.append(count)                       # list에 각 칸에 있을 때 미생물 수 append
    answer = max(answer_list)                               # 그 list에서 최대 미생물 수를 답안으로
    print(f'#{test_case} {answer}')