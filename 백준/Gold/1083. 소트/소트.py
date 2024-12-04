import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
    move_ind = min(s+i+1, n)
    max_ind = nums.index(max(nums[i:move_ind]))

    for j in range(max_ind, i , -1):
        nums[j] , nums[j-1] = nums[j-1], nums[j]
    s -= (max_ind -i)
    
    if s==0 : break

#     for i in range(n-1):
#         max_ind = nums.index(max(nums[i:s+i+1]))
#         if max_ind != i : break

#     for j in range(max_ind, i , -1):
#         nums[j] , nums[j-1] = nums[j-1], nums[j]
#     s -= (max_ind -i)

#     if s <= 0 : break

print(*nums)