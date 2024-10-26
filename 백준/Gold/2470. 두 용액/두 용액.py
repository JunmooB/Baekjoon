import sys
input = sys.stdin.readline


n = int(input())
nums = sorted(list(map(int, input().split())))
res = 0

start = 0
end = n-1
res = int(2e9)
res_left, res_right = start , end
while start<end:
    if abs(nums[start] + nums[end]) < abs(res):
        res_left, res_right = start, end
        res = nums[start] + nums[end]
    
    if nums[start] + nums[end] < 0:
        start += 1
    elif nums[start] + nums[end] > 0:
        end -= 1
    else:
        res_left, res_right = start, end
        break
print(nums[res_left], nums[res_right])