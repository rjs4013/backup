# T = int(input())
# for test_case in range(1, T+1):
#     N, M, K = map(int, input().split())
#     arrive = list(map(int, input().split()))
#     rep = 1
# #붕어빵을 만들 수 있는 개수 K를 예약한 사람 수 N에 맞춰서 M*REP 식에 맞는 REP 구하기
#     if K < N and N % K != 0: rep = N//K + 1
#     elif K < N and N % K == 0: rep = N//K
#     else: rep = 1
#
#     arrive.sort()
#
#     longwait = max(arrive)
#     mametime = rep * M
#
#
#     for x in range(1, N):
#         if
#
#
#     for i in range(N):
#         if arrive[i] < M:
#             print(f'#{test_case} Impossible')
#             break
#     else:
#         if M == N == K: print(f'#{test_case} Possible')
#         else:
#             if mametime > longwait: print(f'#{test_case} Impossible')
#             elif mametime <= longwait: print(f'#{test_case} Possible')