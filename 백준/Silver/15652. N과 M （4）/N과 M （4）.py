n, m = map(int, input().split())
visited = [False] * (n+1)
ans = []

def backtracking(temp):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    else:
        for i in range(temp, n+1): #1부터 n까지 탐색
            ans.append(i)
            backtracking(i)
            ans.pop()

backtracking(1)