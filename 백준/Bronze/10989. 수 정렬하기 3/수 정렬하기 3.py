import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * 10001
for i in range(n):
    temp = int(input())
    nums[temp] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)