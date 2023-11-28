import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
nums = list(range(1,n+1))
nums = deque(nums)

while True:
    if len(nums) == 1:
        print(nums[0])
        break
    else:
        nums.popleft()
        temp = nums.popleft()
        nums.append(temp)