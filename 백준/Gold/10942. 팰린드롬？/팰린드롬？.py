import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
dp = [[0] * (n) for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0
for cnt in range(n-2):
    for i in range(n-2-cnt):
        j = i+2+cnt
        if nums[i]==nums[j] and dp[i+1][j-1]==1 :
            dp[i][j]=1

for _ in range(m):
    s , m = map(int, input().split())
    print(dp[s-1][m-1])