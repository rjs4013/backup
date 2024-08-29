# import sys
# sys.stdin = open("input (2).txt", "r")

def is_palindrom(string): # 회문 확인
    left, right = 0, len(string) -1
    while left < right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    else:
        return True

def long_palindrom(arr, N):
    max_length = 1

    for i in range(N):
        for length in range(N, 1, -1):
            for start in range(N - length + 1):
                if is_palindrom(arr[i][start:start+length]):
                    if length > max_length:
                        max_length = length

                if is_palindrom([arr[j][i] for j in range(start, start + length)]):
                    if length > max_length:
                        max_length = length

    return max_length


for _ in range(1, 11):
    test_case = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    result = long_palindrom(arr, N)
    print(f"#{test_case} {result}")
