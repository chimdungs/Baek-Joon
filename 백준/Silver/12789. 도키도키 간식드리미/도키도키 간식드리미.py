import sys
from collections import deque

input = sys.stdin.readline
n = int(input()) 

d = deque(map(int,input().split()))    

temp = []       #가운데 빠지는 (임시 저장되는 용도)=> stack 자료 구조 이용
output = []     #최종 나가는 통로
target = 1

while True:
    if target > n:
        break
    elif len(temp) > 0 and temp[-1] == target: 
        output.append(temp.pop())
        target += 1     
    elif len(d) > 0 and d[0] == target:
        output.append(d.popleft())
        target +=1
    elif len(d) > 0:
        temp.append(d.popleft())
    else:
        break

if len(output) == n: #전부나왔다(성공)
    print("Nice")
else:
    print("Sad")