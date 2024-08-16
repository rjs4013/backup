def view_buildings(N, building_list):
    totalview = 0
    for i in range(2, N - 1):
        if building_list[i - 2] < building_list[i] > building_list[i - 1] and building_list[i + 1] < building_list[i] > \
                building_list[i + 2]:
            a = max(building_list[i - 2], building_list[i - 1], building_list[i + 1], building_list[i + 2])
            totalview += (building_list[i] - a)
    return totalview


T = 10
for i in range(T):
    N = int(input())
    buildings = list(map(int, input().split()))
    print(f'#{i + 1} {view_buildings(N, buildings)}')