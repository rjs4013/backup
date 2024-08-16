import sys
sys.stdin = open("input.txt","r")


T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = arr[:]
    for x in range(N):
        for y in range(N-x-1):
            if new_arr[y] > new_arr[y+1]:
                new_arr[y], new_arr[y+1] = new_arr[y+1], new_arr[y]
    answer = 0
    for q in new_arr:
        if answer < new_arr.index(q) - arr.index(q):
            answer = new_arr.index(q) - arr.index(q)
    print(f'#{i+1} {answer}')



