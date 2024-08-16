import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    a = len(arr)
    for i in range(a):
        for j in range(a-i-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    answer_arr = ' '.join(map(str, arr))
    print(f'#{test_case} {answer_arr}')