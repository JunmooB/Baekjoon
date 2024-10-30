import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
sum_2 = set()
for i in range(n):
    for j in range(n):
        sum_2.add(nums[i] + nums[j])

res = 0
for i in range(n-1, -1, -1):
    for j in range(n):
        if (nums[i] - nums[j]) in sum_2:
            if nums[i] > res:
                res = nums[i]                
print(res)