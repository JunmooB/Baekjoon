import sys
input = sys.stdin.readline

def bfs(arr, nums, index, cnt):
    if cnt == 6:
        print(*arr)
        return
    else:
        for i in range(index, len(nums)):
            arr[cnt] = nums[i]
            bfs(arr, nums, i+1, cnt+1)


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    arr = [0] * 6
    bfs(arr, nums[1:], 0, 0)
    print()