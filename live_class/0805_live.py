# 고지식한 패턴 검색

# t = 'TTTTTATTAATA'
# p = 'TTA'
# N = len(t)
# M = len(p)
# cnt = 0
# for i in range(N-M+1):  # 비교 시작 위치
#     for j in range(M):
#         if t[i+j] != p[j]:
#             break       #for j가 브레이크, 다음 글자부터 비교 시작
#     else:               # for j가 중단 없이 반복되면
#         cnt += 1        # 패턴 개수 1증가
# print(cnt)

# KMP 알고리즘

def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing
    j = 0 # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1,M):
        lps[i] = j # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print(lps)
    # search
    i = 0 # 비교할 텍스트 위치
    j = 0 # 비교할 패턴 위치
    while i < N or j <= M:
        if j == -1 or t[i] == p[j]:  # 첫 글자가 불일치했거나, 일치하면
            i += 1
            j += 1
        else: # 불일치
            j = lps[j]
        if j == M: # 패턴을 찾을 경우
            print(i-M, end=' ') # 패턴의 인덱스 출력
            j = lps[j]
    print()
    return

t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
