import sys
input = sys.stdin.readline

n , m = map(int, input().split())
level_list = [input().split() for _ in range(n)]
# level_list.sort(key=lambda x: int(x[1]))

chars = [int(input().strip()) for _ in range(m)]
for char in chars:
    left = 0
    right = n
    result = 0
    while left<=right:
        mid = (left+right) // 2
        if int(level_list[mid][1]) >= char:
            right = mid -1
            result = mid
        else:
            left = mid + 1
    print(level_list[result][0])