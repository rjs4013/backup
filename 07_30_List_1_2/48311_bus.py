T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_number = list(map(int, input().split())) + [N]
    a = 0
    i = 0
    count = 0
    while i + K < N:
        if a == 1:
            break
        for j in range(len(bus_number) - 1):
            if i + K == bus_number[j]:
                i = bus_number[j]
                count += 1
            elif i + K > bus_number[j] and i + K < bus_number[j + 1]:
                i = bus_number[j]
                count += 1
            elif i + K < bus_number[j] and i + K < bus_number[j + 1]:
                a = 1
                count = 0
                break

    print(f'#{test_case} {count}')