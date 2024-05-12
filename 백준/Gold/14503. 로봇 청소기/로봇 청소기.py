import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x, y, d = map(int, input().split())  # (x, y) 에서 로봇 청소기 청소 시작함
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
#print(maps)
dx = [-1,0,1,0]
dy = [0,1,0,-1]      # 북(0),동(1), 남(2), 서(3)

cleaned = []         # 청소된 칸의 상태 저장
for i in range(n):
    cleaned.append([0] * m)
ans = 0
while True:
    if maps[x][y] == 0:             # 현재 칸(시작 칸)이 청소되지 않았다면(1번)
        cleaned[x][y] = 1
        temp = 0
        for i in range(4):          # 주변 4 칸을 탐색
            nd = (d - 1) % 4  # 반시계 방향으로 회전
            nx = x + dx[nd] ; ny = y + dy[nd]
            if 0<= nx <n and 0<= ny <m and maps[nx][ny] == 0 and not cleaned[nx][ny]:   # 청소 안된 빈칸(0)이 있는 경우(3번)
                x, y = nx, ny   # 전진
                d = nd
                break
            elif maps[nx][ny] == 1 or cleaned[nx][ny]:  # 벽이거나 청소된 칸인 경우
                temp += 1
                d = nd

        if temp == 4:               # 주변 4칸이 벽이거나 청소된 칸인 경우(2번)
            back_d = (d + 2) % 4      # 후진이라 180도 회전이라고 생각
            back_x, back_y = x + dx[back_d], y + dy[back_d]
            if 0<= back_x < n and 0<= back_y <m and maps[back_x][back_y] == 0:
                x, y = back_x, back_y   # 후진
            else:                       # 후진못하는 경우 종료
                for row in cleaned:
                    ans += sum(row)
                print(ans)
                exit(0)