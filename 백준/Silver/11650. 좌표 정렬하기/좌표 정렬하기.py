import sys
input  = sys.stdin.readline

n = int(input())
xy_list = []
for i in range(n):
    xy_list.append(list(map(int, input().split())))

def merge_sort(x_list):
    if len(x_list) > 1:  #x좌표에 대한 합병정렬 수행
        mid = len(x_list) // 2
        L = x_list[:mid]
        R = x_list[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                x_list[k] = L[i]
                i += 1
            else:
                x_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            x_list[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            x_list[k] = R[j]
            j+=1
            k+=1
    

merge_sort(xy_list)
for m in range(len(xy_list)):
    print(xy_list[m][0], xy_list[m][1])