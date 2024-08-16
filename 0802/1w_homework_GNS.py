# 버블 정렬(실행 시간 김)
# T = int(input())
# for t in range(1, T+1):
#     test_case, number = list(map(str, input().split()))
#     numbers = int(number)
#     n_dict = {}
#     num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     for i in range(len(num_list)):
#         n_dict[num_list[i]] = i
#     arr = list(map(str, input().split()))
#     n_arr = []
#     for z in range(numbers):
#         n_arr.append(n_dict[arr[z]])
#
#     for x in range(numbers-1, 0, -1):
#         for y in range(0, x):
#             if n_arr[y] > n_arr[y+1]:
#                 n_arr[y], n_arr[y+1] = n_arr[y+1], n_arr[y]
#
#     n2_arr = []
#     for u in range(numbers):
#         for k,v in n_dict.items():
#             if v == n_arr[u]:
#                 n2_arr.append(k)
#
#     print(' '.join(map(str, n2_arr)))

# 카운팅 정렬로 풀기
T = int(input())
for _ in range(1, T+1):
    tc, n = input().split()
    words = input().split()
    max_value = 9
    base_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count_list = [0] * (max_value + 1) # 0부터 9까지 카운트 저장할 공간 만들기

    for i in range(len(base_number)):
        for word in words:
            if base_number[i] == word:
                count_list[i] += 1
    answer_list =[]
    for x in range(len(base_number)):
        for _ in range(count_list[x]):
            answer_list.append(base_number[x])
    real_answer = ' '.join(answer_list)
    print(f'{tc} {real_answer}')





