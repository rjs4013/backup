T = int(input())
for i in range(T):
    N = int(input())
    count = [0, 0, 0, 0, 0]
    numbers = [2, 3, 5, 7, 11]
    for x in range(len(numbers)):
        while N % numbers[x] == 0:
            N //= numbers[x]
            count[x] += 1
    new_count = ' '.join(map(str, count))
    print(f'#{i+1} {new_count}')