import sys
input = sys.stdin.readline
n = int(input())
idx = []
for _ in range(n):
    idx.append(int(input()))

f = [0]*101

for i in range(1,101):
    if i <= 3:
        f[i] = 1
    elif i <= 5:
        f[i] = 2
    else:
        f[i] = (f[i - 5] + f[i - 1])

for j in range(n):
    print(f[idx[j]])