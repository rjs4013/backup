def typing(pattern, search):
    pattern_idx = 0
    search_idx = 0
    result = 0
    answer = len(search)
    while search_idx < len(search):
        if search[search_idx] != pattern[pattern_idx]:
            search_idx = search_idx - pattern_idx + 1
            pattern_idx = 0
            continue

        pattern_idx += 1
        search_idx += 1

        if pattern_idx == len(pattern):
            answer = answer - len(pattern) + 1
            pattern_idx = 0
    return answer


T = int(input())
for test_case in range(1, T+1):
    A,B = input().split()
    print(f'#{test_case} {typing(B, A)}')