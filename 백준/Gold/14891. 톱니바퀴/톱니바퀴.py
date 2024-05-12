import sys
from collections import deque

input = sys.stdin.readline

wheel = []
for i in range(4):
    wheel.append(deque(map(int, input().rstrip())))

k = int(input())    # 회전 횟수 k
rotate = []
for i in range(k):
    rotate.append(list(map(int, input().split())))  # 회전할 톱니바퀴번호(1~4), 방향(1,-1)
def move(w_list : deque, direction):
    if direction == 1:      # 시계방향으로 회전
        w_list.appendleft(w_list.pop())
    else:                   # 반시계방향으로 회전
        w_list.append(w_list.popleft())
    return w_list

def rotations(act):
    wheels_rotate = [0] * 4
    wheels_rotate[act[0]-1] = act[1]   # 방향 표시(회전 한다는 뜻)
    for i in range(act[0]-1, 3):       # 우측방향으로 쭉 탐색
        if wheel[i][2] != wheel[i+1][-2] and wheels_rotate[i] !=0 :
            wheels_rotate[i+1] = -wheels_rotate[i]
    for i in range(act[0]-1, 0, -1):    # 좌측방향으로 쭉 탐색
        if wheel[i][-2] != wheel[i-1][2] and wheels_rotate[i] != 0:
            wheels_rotate[i-1] = -wheels_rotate[i]

    for i in range(4):
        if wheels_rotate[i] != 0:
            move(wheel[i], wheels_rotate[i])
for act in rotate:
    rotations(act)

print(wheel[0][0] * 1 + wheel[1][0] * 2 + wheel[2][0] * 4 + wheel[3][0] * 8)