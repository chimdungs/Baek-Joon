import sys


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
cnt = []

# 반복문을 통해 체스판을 확인(8x8 범위로 짜른다.)
for i in range(n - 7):
    for j in range(m - 7):
        w = 0 # w로 시작하는 경우
        b = 0 # b로 시작하는 경우
        
        # 8x8 범위 체스판을 확인
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                # 행과 열의 합이 짝수, 홀수이면 각각 일정한 색을 가지게 된다.
                if (l + k) % 2 == 0:
                    if graph[k][l] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if graph[k][l] != 'B':
                        w += 1
                    else:
                        b += 1
        cnt.append(w)
        cnt.append(b)

# 일정한 색중에 제일 적은 다른 색의 개수를 출력 
print(min(cnt))