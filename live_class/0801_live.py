def sequential_search(a, n, key):
    i = 0
    while i < n and a[i]!=key:
        i = i + 1
    if i < n : return
    else : return -1



def sequentialSearch2(a, n, key):
    i = 0
    while i<n and a[i]<key:
        i = i + 1
    if i < n and a[i] == key:
            return i
    else:
            return -1



def binarySearch(a,N,key):
    start = 0       # 시작 원소 인덱스
    end = N - 1     # 마지막 원소 인덱스
    while start <= end:                # 남은 구간이 있으면...
        middle = (start+end)//2
        if a[middle] == key:    # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False


def selection_sort(arr, N):         # arr 정렬대상, N 크기
    for i in range(N-1):            # 주어진 구간에 대해... 기준 위치 i를 정하고
        min_idx = i                 # 최솟값 위치를 기준 위치로 가정
        for j in range(i+1, N):     # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 구간의 최솟값을 기준위치로 이동
    return arr

A = [2, 7, 5, 3, 4]
selection_sort(A, len(A))


def select(arr, k):
    for i in range(0,k):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index] , arr[i]
    return arr[k-1]