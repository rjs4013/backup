T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    cnt = 0
    answer = 'Possible'
    for i in arrive:
        cnt += 1
        if (i//M)*K < cnt:
            answer = 'Impossible'
            break
    print(f'#{test_case} {answer}')