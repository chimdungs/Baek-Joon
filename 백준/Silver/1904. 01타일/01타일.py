n = int(input())

f = [0]*(1000000+1)
# DP로 피보나치수열 구현
for i in range(n+1):
    if i == 1 or i == 2:
        f[i] = i
    else:
        f[i] = (f[i-1] + f[i-2]) % 15746
print(f[n])