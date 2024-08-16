# N, M, R = map(int,input().split())
# arr = [[0] +list(map(int,input().split()))+[0] for _ in range(N)]
# arr.insert(0,[0]*(M+2))
# arr.append([0]*(M+2))
# for k in range(R):
#     for i in range(1, N):
#         for j in range(1, M+1):
#             if i == 1 and i < j:
#                 arr[i][j] = arr[i][j+1]
#             elif i == N and i < j:
#                 arr[i][j] = arr[i][j-1]
#             elif ij < i:
#                 arr[i][j] = arr[i-1][j]
#             elif i == j:
#                 arr[i][j] = arr[i+1][j]


