n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))

def merge_sort(ls):
    if len(ls) > 1:
        mid = len(ls) // 2
        L = ls[:mid]
        R = ls[mid:]

        merge_sort(L)   #재귀호출
        merge_sort(R)   #재귀호출

        i = j = k = 0  #i = Left내에서 움직일 인덱스/
                       #j = Right내에서 움직일 인덱스/
                       #k = 비교횟수에 대한 인덱스
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                ls[k] = L[i]
                i += 1
            else:
                ls[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            ls[k] = L[i] #switch한거 말고 나머지그냥 복사
            i += 1
            k += 1
        while j < len(R):
            ls[k] = R[j]
            j += 1
            k += 1

merge_sort(ls)
for i in range(n): #정답 형식에 맞게 출력
    print(ls[i])