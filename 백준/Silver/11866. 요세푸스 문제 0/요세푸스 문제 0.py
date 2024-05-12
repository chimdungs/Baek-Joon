from collections import deque

n, k =  map(int, input().split())
q = deque([i+1 for i in range(n)])

ans = []
while True:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(str(q.popleft()))    
    if len(q) == 0:
        break
    
print("<"+', '.join(ans)+">")