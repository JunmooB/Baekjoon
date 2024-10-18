import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * (int(1e6)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, int(1e6) + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for i in range(t):
    n = int(input())
    print(dp[n])