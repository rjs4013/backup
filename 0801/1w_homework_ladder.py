# T = 10
# for test_case in range(1, T + 1):
#     N = 100
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     current_idx = 0
#     di = [0, 0, -1]
#     dj = [1, -1, 0]
#     start_j = 0
#     for x in range(N):
#         if arr[N-1][x] == 2:
#             start_j = x
#     for i in range(N-1, -1, -1):
#         for j in range(N-1, -1, -1):
#             for k in range(3):
#                 ni = i + di[k]
#                 if i == 99:
#                     nj = start_j + dj[k]
#                 else:
#                     nj = j + dj[k]
#                     if 0<=ni<N and 0<=nj<N:
#                         if arr[ni][nj] == 1:
#                             i, j = ni, nj
#                             ni += di[k]
#                             nj += dj[k]
#                             if ni == 0:
#                                 print(nj)

# T = 10
# for test_case in range(1, T + 1):
#     a = int(input())
#     N = 100
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     di = [-1, 0, 0,]
#     dj = [0, 1, -1]
#     start_j = 0
#     for x in range(N):
#         if arr[N-1][x] == 2:
#             start_j = x
#
#     i = N - 1
#     j = start_j
#
#     while i > 0:
#         for k in range(3):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if k == 2:
#                 while arr[ni][nj+1] != 1 and arr[ni][nj-1] != 1:
#                     if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
#                         while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
#                             i, j = ni, nj
#                             ni += di[k]
#                             nj += dj[k]
#                         break
#             else:
#                 if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
#                     while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
#                         i, j = ni, nj
#                         ni += di[k]
#                         nj += dj[k]
#                     break
#     print(j)

T = 10
for _ in range(T):
    a = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    start_j = 0
    for x in range(N):
        if arr[N-1][x] == 2:
            start_j = x

    i, j = N - 1, start_j
    while i > 0:
        if j > 0 and arr[i][j-1] == 1:
            while j > 0 and arr[i][j-1] == 1:
                j -= 1
            i -= 1
        elif j < N - 1 and arr[i][j+1] == 1:
            while j < N - 1 and arr[i][j+1] == 1:
                j += 1
            i -= 1
        else:
            i -= 1

    print(f'#{a} {j}')