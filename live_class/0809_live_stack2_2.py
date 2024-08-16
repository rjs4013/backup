# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i                  # 0번째 원소
#     for j in range(2):
#         bit[1] = j              # 1번째 원소
#         for k in range(2):
#             bit[2] = k          # 2번째 원소
#             for l in range(2):
#                 bit[3] = l      # 3번째 원소
#                 print(bit)      # 생성된 부분집합 출력

# -------------------------------------------------------------

# def backtrack(a,k,n): # a 주어진 배열, k 결정할 원소, n 원소 개수
#     c =[0] * MAXCANDIDATES
#
#     if k == n:
#         process_solution(a,k) # 답이면 원하는 작업을 한다
#     else:
#         ncandidates = construct_candidates(a,k,n,c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a,k+1,n)
#
# def construct_candidates(a,k,n,c):
#     c[0] = True
#     c[1] = False
#     return  2
#
# def proceess_solution(a,k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end = '')
#     print()
#
# MAXCANDIDATES = 2
# NMAX = 4
# a = [0] * NMAX
# num = [1,2,3,4]
# backtrack(a, 0, 3)
# -----------------------------------------------------------------
