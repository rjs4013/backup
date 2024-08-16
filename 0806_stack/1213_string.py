T = 10
for _ in range(T):
    test_case = input()
    pattern_text = input()
    search_text = input()
    result = 0

    pattern_idx = 0
    search_idx = 0

    while search_idx < len(search_text):
        if search_text[search_idx] != pattern_text[pattern_idx]:
            search_idx = search_idx - pattern_idx + 1
            pattern_idx = 0
            continue

        pattern_idx += 1
        search_idx += 1

        if pattern_idx == len(pattern_text):
            result += 1
            pattern_idx =0
            search_idx = search_idx - pattern_idx + 1

    print(f'#{test_case} {result}')
