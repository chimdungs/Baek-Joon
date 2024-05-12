n, m = map(int, input().split())
visited = [False] * (n+1) #왜 n이 아니고 n+1인가
ans = []

def dfs(temp):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(temp, n + 1):
        if visited[i]:  #방문한 곳 패스(가지치기)
            continue
        visited[i] = True
        ans.append(i)   #중복이 아니면 숫자 i를 ans에 추가
        dfs(i + 1)           #재귀호출
        ans.pop()       #다시 찾기 위해 앞에꺼(i) 삭제
        visited[i] = False#마찬가지로 false처리

dfs(1)