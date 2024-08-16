T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 최솟값을 매우 큰 값으로 초기화
    min_paint = float('inf')

    # 흰색 영역의 끝을 i, 파란색 영역의 끝을 j라고 함
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            paint_count = 0

            # 흰색 영역 계산
            for w in range(0, i):
                for k in range(M):
                    if arr[w][k] != 'W':
                        paint_count += 1

            # 파란색 영역 계산
            for b in range(i, j):
                for k in range(M):
                    if arr[b][k] != 'B':
                        paint_count += 1

            # 빨간색 영역 계산
            for r in range(j, N):
                for k in range(M):
                    if arr[r][k] != 'R':
                        paint_count += 1

            # 최소 색칠 횟수 갱신
            min_paint = min(min_paint, paint_count)

    print(f"#{test_case} {min_paint}")