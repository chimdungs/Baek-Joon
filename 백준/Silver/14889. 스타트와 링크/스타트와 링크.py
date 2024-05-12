import sys
def diff(idx_ls):  # 차이 계산해서 ans에 추가하는 함수
    others_idx = list(set(range(1, n + 1)) - set(idx_ls))   #다른 팀에 들어가는 인덱스
    start = 0
    for i in range(len(idx_ls)):
        for j in range(i+1,len(idx_ls)):
                start += s[idx_ls[i]-1][idx_ls[j]-1] + s[idx_ls[j]-1][idx_ls[i]-1]
    link = 0
    for i in range(len(idx_ls)):
        for j in range(i + 1, len(idx_ls)):
                link += s[others_idx[i]-1][others_idx[j]-1] + s[others_idx[j]-1][others_idx[i]-1]
    sum_list.append(abs(start - link))
    #print(sum_list)
    return None

def pick_num(idx_ls):         # 두 개의 팀으로 찢어서 인덱스 저장하는 코드(순열 이용해서 숫자 뽑는 원리)
    if len(idx_ls) == (n//2):
        #print(idx_ls)
        diff(idx_ls)
        return None

    for i in range(idx_ls[-1]+1 if len(idx_ls)>1 else 1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        idx_ls.append(i)
        pick_num(idx_ls)
        idx_ls.pop()
        visited[i] = False

input = sys.stdin.readline
n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
visited = [False] * (n+1)

sum_list = []
pick_num([])
print(min(sum_list))