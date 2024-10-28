import sys
input = sys.stdin.readline

def binarySearch(e):
    start = 0
    end = len(res_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if res_list[mid] == e:
            return mid
        elif res_list[mid] < e:
            start = mid + 1
        else:
            end = mid - 1    
    return start

n = int(input())
nums = list(map(int, input().split()))
res_list = [nums[0]]

for i in range(1, n):
    if res_list[-1] < nums[i]:
        res_list.append(nums[i])
    else:
        idx = binarySearch(nums[i])
        res_list[idx] = nums[i]
        

print(len(res_list))