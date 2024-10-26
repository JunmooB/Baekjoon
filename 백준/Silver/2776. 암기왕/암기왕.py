import sys
input = sys.stdin.readline

def binary_search(x, nums):
    start = 0
    end = n-1
    
    while start <= end:
        mid = (start+end) // 2
    
        if x < nums[mid]:
            end = mid -1
        elif x > nums[mid]:
            start = mid + 1
        else:
            return 1
    return 0

t = int(input())
while t:
    n = int(input())
    before_nums = list(map(int, input().split()))
    m = int(input())
    after_nums = list(map(int, input().split()))
    
    before_nums.sort()
    for num in after_nums:
        print(binary_search(num, before_nums))
    
    t-=1