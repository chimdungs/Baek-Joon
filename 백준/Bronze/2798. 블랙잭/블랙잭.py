import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int, input().split())
cards = list(map(int,(input().split())))

ans = 0

combs= combinations(cards, 3)

for comb in combs:
    temp_ans = sum(comb)
    
    if ans < temp_ans <= m:
        ans = temp_ans
print(ans)