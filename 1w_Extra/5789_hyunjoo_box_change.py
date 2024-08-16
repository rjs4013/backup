T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = []
    for _ in range(1, N+1):
        boxes.append(_)
    num_box = [0] * N

    L = 0
    R = 0
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        num_box[L-1:R] = [i]*(R-L+1)

    answer = ' '.join(map(str, num_box))
    print(f'#{test_case} {answer}')



