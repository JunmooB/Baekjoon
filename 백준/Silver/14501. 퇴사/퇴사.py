import sys
input = sys.stdin.readline

n = int(input())
s_list = []
dp = [0 for _ in range(n+1)]
for i in range(n):
    day , cost = map(int, input().split())
    s_list.append((day, cost))

for i in range(n):
    for j in range(i + s_list[i][0], n+1):
        if dp[j] < dp[i] + s_list[i][1]:
            dp[j] = dp[i] + s_list[i][1]

print(dp[-1])