def money(N, money_dict):
    key_money = list(money_dict.keys())
    for i in range(8):
        if N // key_money[i] >= 1:
            money_dict[key_money[i]] = N // key_money[i]
            N = N - (N // key_money[i]) * key_money[i]

    answer = list(money_dict.values())
    real = ' '.join(map(str, answer))
    return real


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    money_dict = {
        50000 : 0,
        10000 : 0,
        5000 : 0,
        1000 : 0,
        500 : 0,
        100 : 0,
        50 : 0,
        10 : 0
    }
    print(f'#{test_case} {money(N, money_dict)}')
