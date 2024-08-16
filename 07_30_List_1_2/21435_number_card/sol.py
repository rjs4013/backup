import sys
sys.stdin = open("new.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ai_1 = str(input())
    ai = list(str(ai_1))
    a = '0'
    answer = 0
    for i in range(N):
        count = 0
        # print(ai[i])
        for j in range(i, N):
            # print(ai[j])
            if ai[i] == ai[j]:
                count += 1
        if answer < count and int(a) < int(ai[i]):
            a = ai[i]
            answer = count
    print(f'#{test_case} {a} {answer}')