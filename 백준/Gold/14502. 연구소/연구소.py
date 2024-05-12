import sys
from itertools import combinations
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# 지도 상에 0으로 적혀진 좌표들을 저장해서 확인
zero = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            zero.append((i, j)) # (행, 열)좌표 형태로 저장

# 0인 좌표들 중에서 3개를 골라서 벽을 세워야 한다.
direction = [(-1,0), (1,0), (0,-1), (0, 1)] # 상하좌우 이동방향
virus_location = deque([])
ans = []
for walls in combinations(zero, r = 3): # 3 개 선택
    #print(walls)
    maps_c = deepcopy(maps)
    for i in range(3):
        maps_c[walls[i][0]][walls[i][1]] = 1  # 1(벽)로 바꿈

    # BFS를 수행해서 2를 중심으로 주변의 0을 2로 바꾸는 2번쨰 작업 수행
    for i in range(n):
        for j in range(m):
            if maps_c[i][j] == 2:   #바이러스 있는 곳 저장하는 역할
                virus_location.append((i, j))

    while virus_location:
        row, col = virus_location.popleft()
        for dr, dc in direction:
            r, c = row + dr, col + dc
            if 0 <= r < n and 0 <= c < m and maps_c[r][c] == 0:     #퍼뜨리는 조건
                maps_c[r][c] = 2
                virus_location.append((r, c))
    ans.append(sum(cell == 0 for row in maps_c for cell in row))

print(max(ans))