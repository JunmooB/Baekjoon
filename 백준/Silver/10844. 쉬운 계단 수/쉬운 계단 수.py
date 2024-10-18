import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*(10) for _ in range(100+1)]
dp[1] = [0] + [1]*9

for i in range(2, 100+1):
    for j in range(10):
        # j == 0 or j== 9는 다름
        if j == 0:
            dp[i][j] = (dp[i-1][j+1]) % int(1e9)
        elif j == 9:
            dp[i][j] = (dp[i-1][j-1]) % int(1e9)
        else:   
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % int(1e9)
print(sum(dp[n]) % int(1e9))