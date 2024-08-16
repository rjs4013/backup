def view_buildings(a):
    totalview = 0
    for i in range(len(a),0,-2):
        if a[i] != 0:
            if a[i] > a[i+1] and a[i+1] > a[i+2]:
                totalview += (a[i] - a[i+1])
            elif a[i] > a[i+1] and a[i+1] < a[i+2] and a[i] > a[i+2]:
                totalview += (a[i] - a[i+2])
    return totalview



for i in range(10):
    N = int(input())
    buildings = list(map(int,input().split()))
    print(f'#{i+1} {view_buildings(buildings)}')


