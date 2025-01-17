import sys
input = sys.stdin.readline

t = int(input())
dp = [[0]*(4) for _ in range(int(1e5)+1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, int(1e5)+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009

for i in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)