import sys
input = sys.stdin.readline

n = int(input())
reqs = list(map(int, input().split()))
m = int(input())

if sum(reqs) <= m:
    print(max(reqs))
else:
    left , right = 0, max(reqs) - 1
    while left <= right:
        mid = (left + right) // 2        
        result = 0        
        for req in reqs:
            if req <= mid:
                result += req
            else:
                result += mid
        if result <= m:
            left = mid +1
        else:
            right = mid -1
    print(right)
