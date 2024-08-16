def binary_search(input_list, low, high, key):
    if low > high:
        return

    mid_book = int((low+high)/2)

    if key == mid_book:
        return


T = int(input())
for i in range(T):
    P, Pa, Pb = list(map(int, input().split()))


