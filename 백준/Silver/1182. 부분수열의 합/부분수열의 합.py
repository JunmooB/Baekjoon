import sys
input = sys.stdin.readline

def back(ind, sub_sum):
    global res
    if ind == n:
        return
    
    sub_sum += nums[ind]
    if sub_sum == s:
        res += 1
    back(ind+1, sub_sum)
    
    back(ind+1, sub_sum - nums[ind])
        
n , s = map(int, input().split())
nums = list(map(int, input().split()))
res = 0
back(0, 0)
print(res)