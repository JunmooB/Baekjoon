import sys
input = sys.stdin.readline

def binary_search(nums, search):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > search:
            right = mid -1
        elif nums[mid] == search:
            return 1
        else:
            left = mid+1
    return 0


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
searchs = list(map(int, input().split()))
nums.sort()

for search in searchs:
    print(binary_search(nums, search))