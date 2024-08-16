# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N): # 행을 기준으로 확인
#         col_count = 0
#         col_ans = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 col_count += 1
#             if arr[i][j] == 0 or j == N-1:
#                 if col_count == K:
#                     col_ans = col_count
#
#
# for j in range(N): # 열을 기준으로 확인
#     row_count = 0
#     row_ans = 0
#     for i in range(N):
#         if arr[j][i] == 1:
#             row_count += 1
#         if arr[j][i] == 0 or i == N-1:
#             if row_count == K:
#                 row_ans = row_count
# #---------------------------------------------------
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, k = (map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     total_count = 0
#
# for i in range(N):
#     count = 0
#     for j in range(N):
#         if arr[i][j] == 0:
#             if count == k:
#                 total_count += 1
#             else:
#                 count += 1
#
# for j in range(N):
#     count = 0
#     for i in range(N):
#         if arr[j][i] == 0:
#             if count == k:
#                 total_count += 1
#             else:
#                 count += 1
#
# print(f'#{test_case} {total_count}')