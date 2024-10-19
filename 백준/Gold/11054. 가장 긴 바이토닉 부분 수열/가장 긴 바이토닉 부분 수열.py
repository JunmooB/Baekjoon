import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
reverse_nums = nums.copy()
reverse_nums.reverse()

asce_dp, desc_dp = [1] * n , [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            asce_dp[i] = max(asce_dp[i], asce_dp[j] + 1)
            
for i in range(1, n):
    for j in range(i):
        if reverse_nums[i] > reverse_nums[j]:
            desc_dp[i] = max(desc_dp[i], desc_dp[j] + 1)
desc_dp.reverse()
sums = [a + b for a, b in zip(asce_dp, desc_dp)]
print(max(sums)-1)
