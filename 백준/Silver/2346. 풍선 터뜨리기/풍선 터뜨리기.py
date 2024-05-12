import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deq = deque(list(map(int, input().split())))
idx = deque(list(i+1 for i in range(n))) #1,2,...,n까지 저장된 인덱스 역할의 리스트

ans = []
while len(deq) != 0:
    ans.append(idx.popleft())   # 첫번째 ans = 1도 추가됨
    temp = deq.popleft() #temp = 3

    if deq and temp > 0:         #양수방향으로 움직여야 하는 경우
        for _ in range(temp-1):
            deq.append(deq.popleft())
            idx.append(idx.popleft())

    elif deq and temp < 0:       #음수방향으로 움직여야 하는 경우
        for _ in range(abs(temp)):
            deq.appendleft(deq.pop())
            idx.appendleft(idx.pop())

print(*ans)