T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(str(input()))
    count_list = []
    count = 0
    i = 0
    while i < N:
        if numbers[i] == '1':
            count += 1
            i += 1
            if numbers[N-1] == '1':
                count_list.append(count)
        else:
            count_list.append(count)
            count = 0
            i += 1
    answer = max(count_list)
    print(f'#{test_case} {answer}')