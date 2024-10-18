import sys
input = sys.stdin.readline

n = int(input())
dp = list(range(100000+1))
for i in range(n+1):
    for j in range(1, i):
        if i-j*j <0: break
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1
print(dp[n])