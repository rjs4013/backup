T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    size = input().split()
    answer = 0
    for i in range(N-1):
        count = 1
        for j in range(i,N-1):
            if int(size[j]) < int(size[j+1]):
                count += 1
            elif int(size[j]) >= int(size[j+1]):
                break
        if answer <= count:
            answer = count
    print(f'#{test_case} {answer}')
