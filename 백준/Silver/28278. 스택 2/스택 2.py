import sys
input = sys.stdin.readline
n = int(input())

# Stack 구현
class Stack:
    def __init__(self):
        self.items = []     #스택 초기화

    def is_empty(self):     #명령 4
        if len(self.items) == 0:
            print(1)
        else:
            print(0)   

    def push(self, item):   #명령 1
        self.items.append(item)

    def pop(self):          #명령 2
        if len(self.items) != 0:
            print(self.items[-1])
            return self.items.pop()
        else:
            print(-1)

    def print(self):         #명령5
        if len(self.items) != 0:
            print(self.items[-1])
        else:
            print(-1)

    def size(self):          #명령 3
        print(len(self.items))
    
ls =  [list(map(int, input().split())) for _ in range(n)]
ans = Stack()

for j in range(len(ls)):
    if ls[j][0] == 1:
        ans.push(ls[j][1])
    elif ls[j][0] == 2:
        ans.pop()
    elif ls[j][0] == 3:
        ans.size()
    elif ls[j][0] == 4:
        ans.is_empty()
    else:   #명령5
        ans.print()