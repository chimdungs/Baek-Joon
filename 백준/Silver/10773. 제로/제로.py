import sys
input = sys.stdin.readline

k = int(input())
ls = []
for i in range(k):
    ls.append(int(input()))

ans = []
for i in range(k):
    if ls[i] != 0:
        ans.append(ls[i])
    else:
        ans.pop()

print(sum(ans))