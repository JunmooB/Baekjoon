import sys
input = sys.stdin.readline

n = int(input())
if n>=2:
    dp = [-1] * (n+1)
    dp[0] , dp[1] = 0 , 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
else:
    print(1)