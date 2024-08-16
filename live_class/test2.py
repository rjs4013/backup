arr2 = [[0]*3 for _ in range(2)]    # [[0] * 3] * 2 랑 다름,,, 무조건 for 문으로 돌릴 것
# for i in range(2):
#     print(arr2[i])        # i가 0이면 첫 번째 행 전체
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end= ' ')       # 0 0 0 0 0 0
#     print()                               # 0 0 0
                                          # 0 0 0

# arr = [[1,2,3],[4,5,6]]
# print((len(arr)))   # 2
# print(len(arr[0]))  # 3

### 배열 원소의 모든 합
# sum_a = 0
# for i in range(2):
#     for j in range(3):
#         sum_a += arr2[i][j]
# print(sum_a)

### 최대,최소
# max_v = # 초기값
# min_v = # 초기값
# for i in range(2):
#     sum_a = 0
#     for j in range(3):
#         sum_a += arr2[i][j]
#         if max_v < sum_a:
#             max_v = sum_a
#         if min_v > sum_a:
#             min_v = sum_a
# print(max_v, min_v)

### 열 우선 순회
# for j in range(m):          # 열
#     for i in range(n):      # 행
#         arr2[i][j]          # 필요한 연산 수행

### 지그재그 순회


### 델타를 이용한 2차 배열 탐색
# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
# arr[0...N-1][0...N-1] # N*N 배열
# di[] <- [0, 1, 0, -1]
# dj[] <- [1, 0, -1, 0]
# for i : 0 -> N-1:
#     for j : 0 -> N-1:
#         for k in range(4):
#             ni <- i + di[k]
#             nj <- j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N # 유효한 인덱스면
#                 f(arr[ni][nj])


### 부분집합
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)


###연산자를 사용한 부분집합 구하기
# arr = [3,6,7,1,5,4]
# n = len(arr)
#
# for i in range(1 << n): # 1<<n: 부분 집합의 개수
#     for j in range(n):  # 원소의 수만큼 비트 비교
#         if i & (1<<j): # i의 j번 비트가 1인 경우
#             print(arr[j], end = ', ')  # j번 원소 출력
#     print()
# print()