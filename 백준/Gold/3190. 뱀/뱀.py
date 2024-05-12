import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
maps = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):  # 사과의 위치
    x, y = map(int, input().split())
    maps[x][y] = 2
snake = {}
l = int(input())
for _ in range(l):  # 뱀의 방향변환정보
    sec, direct = input().split()
    snake[int(sec)] = direct

time = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 1, 1
maps[y][x] = 1
i = 0
snakes = deque([(1, 1)])

while True:
    nx, ny = x + dx[i], y + dy[i]
    if nx <= 0 or ny <= 0 or nx > n or ny > n or (nx, ny) in snakes: # 게임종료조건
        break
    if maps[ny][nx] != 2:        # 1)사과 먹지 못하는 경우
        a, b = snakes.popleft()     # => 꼬리를 없앤다
        maps[b][a] = 0             # 꼬리 위치했던 칸 비워줌
    x, y = nx, ny                    # 2)사과 먹은 경우
    maps[y][x] = 1                 # 뱀 이동함(위치 변경)
    snakes.append((nx, ny))         # 뱀 길이가 늘어난다
    time += 1                       # 한번 이동했기 때문에 1초 추가

    if time in snake.keys():
        if snake[time] == 'D':      # 오른쪽 방향으로 회전되게 방향 변환
            i = (i+1) % 4
        else:                       # 왼쪽 방향으로 회전
            i = (i-1) % 4

print(time+1)