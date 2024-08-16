T = int(input())
for test_case in range(1,T+1):
    N, K = map(int, input().split())
    complete = list(map(int, input().split()))
    numbers = []
    check = [0] * (N+1)
    answer = []
    for x in range(1, N+1):
        numbers.append(x)
    for i in complete:
        check[i] = 1
    for j in range(1, len(check)):
        if check[j] == 0:
            answer.append(numbers[j-1])
    a = ' '.join(map(str,answer))
    print(f'#{test_case} {a}')