def binary(arr, l, r, find_key):
    over = -1 # 오오 또는 왼왼 일때 바로 false 출력
    while l <= r :
        mid = (l + r) // 2
        if find_key == arr[mid]:
            return True
        elif find_key < arr[mid]:
            if over == 0:
                return False
            r = mid - 1
            over = 0
        elif find_key > arr[mid]:
            if over == 1:
                return False
            l = mid + 1
            over = 1
    return False

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    a_arr.sort()
    b_arr.sort()

    cnt = 0
    for find_key in b_arr:
        if binary(a_arr, 0, N - 1, find_key):
            cnt += 1

    print(f'#{test_case} {cnt}')
