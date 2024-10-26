import sys
input = sys.stdin.readline

def binary_search(x, nums):
    start = 0
    end = m-1
    
    while start <= end:
        mid = (start+end) // 2
    
        if x <= nums[mid]:
            end = mid -1
        elif x > nums[mid]:
            start = mid + 1   
    return start

t = int(input())
while t:
    n , m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = sorted(list(map(int, input().split())))
    res = 0
    for a in a_list:
        # print(binary_search(a, b_list))
        res += binary_search(a, b_list)
    print(res)
    
    t-=1