import sys
input = sys.stdin.readline


n = int(input())
nums = sorted(list(map(int, input().split())))
res = 0
for i in range(len(nums)):
    target = nums[i]
    start = 0
    end = len(nums)-1
    while start<end:
        if nums[start] + nums[end] < target:
            start += 1
        elif nums[start] + nums[end] > target:
            end -= 1
        else:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                res += 1
                break
print(res)