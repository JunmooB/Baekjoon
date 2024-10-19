import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for i in range(n):
    temp = list(map(int, input().split()))
    numbers.append(temp)
numbers.append([])
numbers.reverse()
dp = [[] for _ in range(n+1)]
dp[1] = numbers[1]
for i in range(2, n+1):
    for j in range(n-i+1):
        temp = max(dp[i-1][j], dp[i-1][j+1]) + numbers[i][j]
        dp[i].append(temp)
print(dp[-1][0])