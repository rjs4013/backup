from collections import deque

T = 10
for _ in range(1,T+1):
    testcase = int(input())
    password = deque(list(map(int, input().split())))
    count = 1

    while password[-1] > 0:
        pop_data = password.popleft()
        pop_data -= count
        if pop_data < 0 :
            pop_data = 0
        password.append(pop_data)
        count += 1
        if count > 5:
            count = 1
    answer = ' '.join(map(str, password))
    print(f'#{testcase} {answer}')