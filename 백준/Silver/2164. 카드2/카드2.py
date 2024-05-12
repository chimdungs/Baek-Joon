from collections import deque

n = int(input())

q = deque([i+1 for i in range(n)])

for i in range(n-1):
    q.popleft() #가장 위에 있는(왼쪽의) 원소 삭제
    q.append(q.popleft())

print(q[-1])