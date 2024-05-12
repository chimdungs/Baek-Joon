import sys
from collections import deque

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
call = list(map(int, input().split()))  #명령 저장

# x, y = 주사위를 놓은 곳의 위치좌표(초기상태는 input으로 받는 상황)

dice_num = [0, 0, 0, 0, 0, 0]                       # 주사위 초기 놓여진 상태
#dice_num = [1, 3, 6, 4, 2, 5]          # 전개도 참고(idx = 2가 주사위의 아랫면이 되게 설정)

def move(dice_num, direction):
    if direction == 1:      #동쪽
        return [dice_num[3], dice_num[0], dice_num[1], dice_num[2], dice_num[4], dice_num[5]]
    elif direction == 2:    #서쪽
        return [dice_num[1], dice_num[2], dice_num[3], dice_num[0], dice_num[4], dice_num[5]]
    elif direction == 3:    #북쪽
        return [dice_num[5], dice_num[1], dice_num[4], dice_num[3], dice_num[0], dice_num[2]]
    else:                   #남쪽
        return [dice_num[4], dice_num[1], dice_num[5], dice_num[3], dice_num[2], dice_num[0]]

ans = []
dx = [0, 0 ,-1, 1]  # i=1:동, i=2:서
dy = [1, -1, 0, 0]  # i = 3:북, i=4:남
#print(call)
for c in call:      # k번의 명령에 대해 반복문 수행
    nx = x + dx[c - 1]
    ny = y + dy[c - 1]
    if nx >= n or ny >= m or nx < 0 or ny < 0:  # 주사위 바깥으로 이동시키는 경우, 해당명령 무시
        continue
    for i in range(1, 4+1):
        if c == i:                    # _쪽으로 이동
            dice_num = move(dice_num, direction = i)
            if maps[nx][ny] == 0:             # 움직였는데 지도 좌표상 0이 적혀있는 경우
                maps[nx][ny] = dice_num[2]    # 주사위 바닥에 있는 숫자가 지도로 복사됨
            else:
                dice_num[2] = maps[nx][ny]    # 지도에 적힌 숫자가 주사위에 복사됨
                maps[nx][ny] = 0
    x,y = nx, ny
    print(dice_num[0])   # 주사위 윗면의 숫자 출력
