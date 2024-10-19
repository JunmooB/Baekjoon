import sys
input = sys.stdin.readline

n = int(input())
wines = [0]
for i in range(n):
    wine = int(input())
    wines.append(wine)
dp = [0] * (n+1)
dp[1] = wines[1]
if n== 1:
    print(dp[1])
    exit()
dp[2] = wines[2] + dp[1]
if n==2:
    print(dp[n])
    exit()
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3] +wines[i] + wines[i-1])
print(dp[n])