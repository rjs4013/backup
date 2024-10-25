'''
- 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 받음
- 두 사람 사이에 선물주고받은 기록이 없거나, 주고 받은 수가 같다면, -> 선물 지수가 더 큰 사람이 선물받음
(선물지수) -> 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값
- 두 사람의 선물 지수도 같다면 선물 주고 받지말기
출력 => 선물을 가장 많이 받을 친구가 받을 선물의 수
friends - 친구들 이름
gifts - 이번달까지 친구들이 주고받은 선물 기록['준사람 받은사람'] -> 공백으로 구분되어 있음
'''


def solution(friends, gifts):
    answer = 0
    
    N = len(friends)
    list_gift = len(gifts)
    arr = [[0] * N for _ in range(N)]
    for i in range(list_gift):
        a, b = map(str, gifts[i].split())
        print(a, b)
    return answer
