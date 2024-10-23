'''
벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.
1.벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다.
2.초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다.
**가능한 다양한 종류의 초밥을 먹으려 함**
N = 벨트 위 초밥 번호
d = 초밥의 가짓 수
k = 연속해서 먹는 접시 수
c = 쿠폰 번호
'''

N, d, k, c = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 0
for i in range(N):
    if i+k+1 <= N:
        eat_list = arr[i:k+i]
    else:
        eat_list = arr[i:] + arr[:k-(N-i)]
    eat_list = set(eat_list)
    eat_list.add(c)
    ans = max(ans, len(eat_list))
print(ans)