def find_start_point(N, start_j, arr):
    visited = [[False] * N for _ in range(N)]
    i, j = 0, start_j
    count = 0

    while i < N - 1:  # 마지막 행까지 이동
        visited[i][j] = True

        # 현재 위치에서 이동할 방향 (아래, 왼쪽, 오른쪽)
        if j > 0 and arr[i][j - 1] == 1 and not visited[i][j - 1]:
            # 왼쪽
            while j > 0 and arr[i][j - 1] == 1:
                j -= 1
                count += 1
            i += 1
        elif j < N - 1 and arr[i][j + 1] == 1 and not visited[i][j + 1]:
            # 오른쪽
            while j < N - 1 and arr[i][j + 1] == 1:
                j += 1
                count += 1
            i += 1
        else:
            # 아래
            i += 1

    return count


T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = float('inf')
    good_start = 0

    for j in range(N):
        if arr[0][j] == 1:  # 출발 위치 검색
            result = find_start_point(N, j, arr)

            if result < answer:
                answer = result
                good_start = j  # 출발 위치 저장

    print(f"#{test_case} {good_start}")