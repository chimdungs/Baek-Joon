# 16234 인구이동
import sys
input = sys.stdin.readline
n, l, r = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n]
# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 국경선을 열지 말지 결정하는 함수 만들기
def dfs(x, y, graph):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if not(visited[nx][ny]) and (l <= abs(graph[nx][ny] - graph[x][y]) <= r):
                open_location.append((nx,ny))
                dfs(nx, ny, graph)
    return open_location

ans = 0
while True:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            open_location = [(i,j)]  # 시작 탐색 위치
            if not visited[i][j]:
                open_location = dfs(i, j, maps)
            if len(open_location) > 1:   # 국경선 여는 국가가 하나 이상이라면
                flag = True; temp = 0
                for x, y in open_location:
                    temp += maps[x][y]
                pop_avg = temp // len(open_location) # 소숫점을 버린다
                for x, y in open_location:   # 지도 업데이트
                    maps[x][y] = int(pop_avg)
    if not(flag):
        print(ans)
        break
    ans += 1