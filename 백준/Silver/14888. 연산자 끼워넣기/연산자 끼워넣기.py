import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))

sym_ls = []
for i in range(4):
    sym = ['+', '-', '*', '//']
    if operator[i] > 0:
        for _ in range(operator[i]):
            sym_ls.append(sym[i])

ans = []
def calculate(operate_order):
    temp = num[0]

    for i in range(n-1):
        if operate_order[i] == '+':
            temp += num[i+1]
        elif operate_order[i] == '-':
            temp -= num[i+1]
        elif operate_order[i] == '*':
            temp *= num[i+1]
        else: #나눗셈 특이연산(C++14기준)
            if temp < 0:
                temp = abs(temp)
                temp //= num[i+1]
                temp = -temp
            else:
                temp //= num[i+1]
    ans.append(temp)
    #print(ans)
    return

operate_order = []
visited = [False] * n
def backtracking():
    if len(operate_order) == (n-1):
        #print(operate_order)
        calculate(operate_order)
        return

    for i in range(len(sym_ls)):
        if visited[i]:
            continue
        visited[i] = True
        operate_order.append(sym_ls[i])
        backtracking()
        operate_order.pop()
        visited[i] = False

backtracking()
print(max(ans))
print(min(ans))