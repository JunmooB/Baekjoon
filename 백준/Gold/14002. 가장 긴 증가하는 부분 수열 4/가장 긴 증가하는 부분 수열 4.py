import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * (1000+1)
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
res = max(dp)      
print(res)
ind = dp.index(res)
str_list = [nums[ind]]
for i in range(ind-1, -1, -1):
    if dp[i] == res-1:
        str_list.append(nums[i])
        res -= 1
str_list.reverse()
print(*str_list)