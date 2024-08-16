def made(N, K, scores):
    for i in range(N-1):
        for j in range(N-i-1):
            if scores[j] < scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
    answer = 0
    for k in range(K):
        answer += scores.pop(0)
    return answer



T = int(input())
for test_case in range(1, T+1):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))
    a = made(N, K, scores)
    print(f'#{test_case} {a}')