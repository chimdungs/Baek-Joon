# 15686 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

homes = [] ; chicken = []
for r in range(n):
    for c in range(n):
        if maps[r][c] == 1:
            homes.append([r,c])
        if maps[r][c] == 2:
            chicken.append([r,c])

def dist(a, b):     # 맨해튼 거리
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

combs = list(combinations(chicken, m))    # m개의 치킨집 선택한 경우의 수(조합) 좌표 저장
ans = []
for chick in range(len(combs)):  # 치킨 집 m개 조합 갯수마다
    # print("m개 선택된 치킨집위치:",combs[chick])
    chicken_dist = 0             # 도시의 치킨거리
    for home in homes:
        temp = []
        # print("집 위치 :", home)
        for i in range(m):
            temp.append(dist(home, combs[chick][i]))
        # print("집에서의 치킨거리", min(temp))
        chicken_dist += min(temp)   # 조합마다의 도시 치킨거리 저장
    ans.append(chicken_dist)
print(min(ans))