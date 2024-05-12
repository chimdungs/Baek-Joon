n = int(input())

ls = []
for i in range(len(str(n))):
    ls.append(int(str(n)[i])) # 각 자릿수를 리스트에 넣어 보관

for j in range(len(ls)-1): # 버블 정렬
    for k in range(j+1,len(ls)):
        if ls[j] < ls[k]:
            temp = ls[j]
            ls[j] = ls[k]
            ls[k] = temp
        else:
            continue

result = int("".join(map(str, ls)))

print(result)