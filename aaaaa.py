def left_shift(arr, n): # 배열, 왼쪽으로 이동시킬 횟수
    new_arr = [None for _ in range(len(arr))]
    for i in range(len(arr)):
        new_arr[i-n] = arr[i]
    return new_arr

def right_shifr(arr, n): # 배열, 오른쪽으로 이동시킬 횟수
    new_arr = [None for _ in range(arr)]
    for i in range(len(arr)):
        new_arr[i] = arr[i-n]
    return new_arr

arr = [1, 2, 3, 4, 5]

ans = right_shifr(arr, 1)
print(ans)