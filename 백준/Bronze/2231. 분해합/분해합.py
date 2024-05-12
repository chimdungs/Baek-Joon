n = int(input())
ans = []
for y in range(1000000): #출력값은 일단 무조건 입력보다 작기때문에 범위를 100000미만으로 설정
    temp = 0
    for i in range(len(str(y))):
        temp += int(str(y)[i])

    if y + temp  == n:
        ans.append(y)
        print(y)
        break
        
if len(ans) == 0:
    print(0)