import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp = [[0] * 2 for _ in range(n)]
dp = [[x for x in nums ]for _ in range(2)]
for i in range(1,n):
    # dp[i][0] = max(dp[i][0], dp[i-1][0]+nums[i])
    # dp[i][1] = max(dp[i-1][0], dp[i-1][1] + nums[i])
    dp[0][i] = max(dp[0][i], dp[0][i-1]+nums[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + nums[i])

print(max(max(dp[0]), max(dp[1])))