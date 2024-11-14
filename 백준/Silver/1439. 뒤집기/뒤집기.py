import sys
input = sys.stdin.readline

nums = str(input())
zeros , ones= 0 , 0
temp = nums[0]
for i in range(1, len(nums)):
    if temp == nums[i]: continue
    else:
        if temp == '0': zeros += 1
        else: ones += 1
        temp = nums[i]
print(min(zeros, ones))